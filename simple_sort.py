import os
import shutil
import logging
from file_traversal import FileTraversal  

class FileOrganizer:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.traverser = FileTraversal(root_dir)
        # Set logging level to WARNING to suppress INFO messages
        logging.getLogger().setLevel(logging.WARNING)

    def organize_files(self):
        """Organize files based on metadata and file type."""
        self.traverser.hybrid_traversal()  # Perform traversal to collect files

        # Collect files for organization
        for entry in os.scandir(self.root_dir):
            if entry.is_file():
                metadata = self._collect_metadata(entry)
                self._move_file(entry, metadata)

    def _collect_metadata(self, entry):
        """Collect metadata for a given file."""
        return {
            'type': entry.name.split('.')[-1],  # File type based on extension
        }

    def _move_file(self, entry, metadata):
        """Move file to the appropriate folder based on its metadata."""
        file_type_folder = os.path.join(self.root_dir, metadata['type'])

        # Create folder if it doesn't exist
        os.makedirs(file_type_folder, exist_ok=True)

        # Move file to the appropriate folder
        try:
            shutil.move(entry.path, file_type_folder)
            logging.info(f"Moved {entry.name} to {file_type_folder}")
        except Exception as e:
            logging.error(f"Failed to move {entry.name}: {e}")

def simple_sort(root_directory):
    organizer = FileOrganizer(root_directory)
    organizer.organize_files()
