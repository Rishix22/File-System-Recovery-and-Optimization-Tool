import os
import pickle

class FileSystem:
    def __init__(self, disk_size=100):
        self.disk_size = disk_size  # Total blocks on disk
        self.bitmap = [0] * disk_size  # Free-space management (0=free, 1=occupied)
        self.directory = {}  # Directory structure {filename: (start_block, size, content)}

    def allocate_blocks(self, size):
        free_blocks = [i for i, b in enumerate(self.bitmap) if b == 0]
        if len(free_blocks) < size:
            return None  # Not enough space
        allocated = free_blocks[:size]
        for block in allocated:
            self.bitmap[block] = 1
        return allocated

    def create_file(self, filename, content):
        if filename in self.directory:
            print(f"Error: File '{filename}' already exists.")
            return
        
        size = len(content)
        allocated_blocks = self.allocate_blocks(size)
        if not allocated_blocks:
            print("Error: Not enough space.")
            return
        
        self.directory[filename] = (allocated_blocks, content)
        print(f"File '{filename}' created successfully.")

    def read_file(self, filename):
        if filename not in self.directory:
            print(f"Error: File '{filename}' not found.")
            return
        
        _, content = self.directory[filename]
        print(f"Contents of '{filename}': {content}")

    def delete_file(self, filename):
        if filename not in self.directory:
            print(f"Error: File '{filename}' not found.")
            return
        
        allocated_blocks, _ = self.directory[filename]
        for block in allocated_blocks:
            self.bitmap[block] = 0
        
        del self.directory[filename]
        print(f"File '{filename}' deleted successfully.")

    def defragment(self):
        print("Performing disk defragmentation...")
        new_directory = {}
        new_bitmap = [0] * self.disk_size
        next_free_block = 0

        for filename, (blocks, content) in self.directory.items():
            size = len(content)
            new_blocks = list(range(next_free_block, next_free_block + size))
            new_directory[filename] = (new_blocks, content)
            for i in range(size):
                new_bitmap[new_blocks[i]] = 1
            next_free_block += size
        
        self.directory = new_directory
        self.bitmap = new_bitmap
        print("Disk defragmentation complete.")

    def backup_system(self):
        with open("filesystem_backup.pickle", "wb") as f:
            pickle.dump((self.bitmap, self.directory), f)
        print("System backup saved.")

    def restore_system(self):
        if not os.path.exists("filesystem_backup.pickle"):
            print("No backup found.")
            return
        
        with open("filesystem_backup.pickle", "rb") as f:
            self.bitmap, self.directory = pickle.load(f)
        print("System restored from backup.")

# Example Usage
fs = FileSystem()
fs.create_file("file1", "hello")
fs.create_file("file2", "world")
fs.read_file("file1")
fs.defragment()
fs.backup_system()
fs.restore_system()
fs.read_file("file2")
