# File System Recovery and Optimization Tool

## Overview
This is a simple **File System Recovery and Optimization Tool** implemented in Python. It simulates a basic file system with functionalities for file creation, deletion, reading, defragmentation, and backup/restore operations.

## Features
- **File Creation**: Create files with dynamically allocated blocks.
- **File Reading**: Retrieve and display file contents.
- **File Deletion**: Remove files and free up storage blocks.
- **Defragmentation**: Optimize storage by reorganizing file allocations.
- **Backup System**: Save the current file system state for recovery.
- **Restore System**: Recover the file system from a saved backup.

## Installation & Usage
### Prerequisites
- Python 3.x

### Running the Tool
1. Clone the repository:
   ```bash
   git clone https://github.com/Rishix22/File-System-Recovery-and-Optimization-Tool.git
   cd File-System-Recovery-and-Optimization-Tool
   ```
2. Run the script:
   ```bash
   python file_system.py
   ```

## Example Usage
```python
fs = FileSystem()
fs.create_file("file1", "hello")
fs.create_file("file2", "world")
fs.read_file("file1")
fs.defragment()
fs.backup_system()
fs.restore_system()
fs.read_file("file2")
```

## Contributing
Feel free to fork the repository, create a new branch, and submit a pull request!

## License
This project is licensed under the MIT License.

