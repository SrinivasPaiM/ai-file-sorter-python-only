# AI File Sorter

## Overview
AI File Sorter is an intelligent file organization system that categorizes and sorts files based on their filenames. It utilizes a machine learning model to predict file categories and automatically moves them to appropriate directories. The system runs entirely in the Python console and does not include a graphical user interface.

## Features
- **AI-Powered Sorting**: Uses a Decision Tree Classifier to categorize files based on their names.
- **Command-Line Based**: Runs in the Python console without a separate frontend.
- **Customizable Output Directory**: Allows users to specify where sorted files should be saved.
- **File Traversal Support**: Efficiently scans directories to identify and sort files.
- **Progress Display**: Shows categorization and sorting updates directly in the console.

## Installation & Setup
### **1. Clone the Repository**
```sh
git clone https://github.com/SrinivasPaiM/ai-file-sorter-python-only.git
cd ai-file-sorter
```

### **2. Update Output Directory**
Edit `advanced_sort.py` and replace the output directory with your desired path:
```python
sorted_output_directory = "your/output/directory/path"
```

### **3. Run the Application**
```sh
python main_interface.py
```

## Usage
1. **Select Files**: The system will prompt you to choose files for sorting.
2. **Choose Output Directory**: Specify where sorted files should be stored.
3. **Review Predictions**: The system predicts categories based on filenames.
4. **Confirm & Sort**: Once confirmed, the files are automatically moved to categorized folders.

## File Structure
```
├── ai-file-sorter/
│   ├── main_interface.py   # Entry point for the sorting system
│   ├── advanced_sort.py    # AI-based sorting logic
│   ├── simple_sort.py      # Basic sorting functionality
│   ├── file_traversal.py   # File scanning and traversal logic
│   ├── README.md           # Project documentation
```

## Contributing
If you’d like to contribute, feel free to fork the repo, make improvements, and submit a pull request.

## License
This project is licensed under the MIT License.

