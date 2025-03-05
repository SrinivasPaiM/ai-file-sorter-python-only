import os
import shutil
import logging
import pickle
from datetime import datetime
from collections import deque
from concurrent.futures import ThreadPoolExecutor, as_completed

class FileTraversal:
    def __init__(self, root_dir, initial_batch_size=10, state_file="traversal_state.pkl"):
        self.root_dir = root_dir
        self.initial_batch_size = initial_batch_size
        self.state_file = state_file
        self.queue = deque()
        self._load_state()
        self.executor = ThreadPoolExecutor(max_workers=os.cpu_count())

    def hybrid_traversal(self):
        """Perform hybrid traversal combining BFS and DFS with parallel processing and dynamic batch processing."""
        if not self.queue:
            self.queue.append(self.root_dir)
        batch_size = self.initial_batch_size
        while self.queue:
            batch_size = self._adjust_batch_size(batch_size)
            batch = self._get_next_batch(self.queue, batch_size)
            futures = [self.executor.submit(self._process_path, path) for path in batch]
            for future in as_completed(futures):
                sub_paths = future.result()
                for path in sub_paths:
                    self.queue.append(path)
            self._save_state()
        self.executor.shutdown()

    def _adjust_batch_size(self, current_batch_size):
        """Adjust the batch size based on system load and available threads."""
        return current_batch_size

    def _get_next_batch(self, queue, batch_size):
        """Get the next batch of paths from the queue."""
        return [queue.popleft() for _ in range(min(batch_size, len(queue)))]

    def _process_path(self, path):
        """Process a single path, collecting sub-paths."""
        sub_paths = []
        try:
            with os.scandir(path) as it:
                for entry in it:
                    if entry.is_file():
                        # Collect file metadata (do not log here)
                        metadata = self._collect_metadata(entry)
                        # Log file move operations only if needed, here suppressed
                    elif entry.is_dir():
                        # Collect directory metadata and add to queue
                        metadata = self._collect_metadata(entry)
                        sub_paths.append(entry.path)
        except PermissionError:
            logging.error(f"Permission denied: {path}")
        except Exception as e:
            logging.error(f"Error processing path {path}: {e}")
        return sub_paths

    def _collect_metadata(self, entry):
        """Collect metadata for a given file or directory entry."""
        try:
            stat = entry.stat()
            metadata = {
                'size': stat.st_size,
                'creation_date': datetime.fromtimestamp(stat.st_ctime),
                'modification_date': datetime.fromtimestamp(stat.st_mtime),
                'type': 'directory' if entry.is_dir() else 'file'
            }
            return metadata
        except Exception as e:
            logging.error(f"Failed to collect metadata for {entry.path}: {e}")
            return {}

    def _save_state(self):
        """Save the traversal state to a file."""
        state = {'queue': list(self.queue)}
        with open(self.state_file, 'wb') as f:
            pickle.dump(state, f)
        logging.info("Traversal state saved.")

    def _load_state(self):
        """Load the traversal state from a file."""
        if os.path.exists(self.state_file):
            with open(self.state_file, 'rb') as f:
                state = pickle.load(f)
                self.queue = deque(state['queue'])
            logging.info("Traversal state loaded.")
        else:
            logging.info("No saved state found, starting fresh.")
