import os
import pickle

class FileSystem:
    def __init__(self, disk_size=100):
        self.disk_size = disk_size  # Total blocks on disk
        self.bitmap = [0] * disk_size  # Free-space management (0=free, 1=occupied)
        self.directory = {}  # Directory structure {filename: (start_block, size)}
        self.storage = [None] * disk_size  # Simulated disk storage

    def create_file(self, filename, size, content):
        if filename in self.directory:
            print(f"Error: File '{filename}' already exists.")
            return
        
        free_blocks = [i for i, b in enumerate(self.bitmap) if b == 0]
        if len(free_blocks) < size:
            print("Error: Not enough space.")
            return
        
        start_block = free_blocks[0]
        for i in range(size):
            self.bitmap[free_blocks[i]] = 1
            self.storage[free_blocks[i]] = content[i] if i < len(content) else ' '
        
        self.directory[filename] = (start_block, size)
        print(f"File '{filename}' created successfully.")

    def read_file(self, filename):
        if filename not in self.directory:
            print(f"Error: File '{filename}' not found.")
            return
        
        start, size = self.directory[filename]
        content = ''.join(self.storage[start:start + size])
        print(f"Contents of '{filename}': {content}")

    def delete_file(self, filename):
        if filename not in self.directory:
            print(f"Error: File '{filename}' not found.")
            return
        
        start, size = self.directory[filename]
        for i in range(start, start + size):
            self.bitmap[i] = 0
            self.storage[i] = None
        
        del self.directory[filename]
        print(f"File '{filename}' deleted successfully.")

    def simulate_crash(self):
        print("Simulating disk crash... Saving backup...")
        with open("backup.fs", "wb") as f:
            pickle.dump((self.bitmap, self.directory, self.storage), f)
        print("Backup successfully saved.")

    def recover_system(self):
        if not os.path.exists("backup.fs"):
            print("No backup found. Recovery failed.")
            return
        
        with open("backup.fs", "rb") as f:
            self.bitmap, self.directory, self.storage = pickle.load(f)
        print("System successfully recovered from backup.")

    def optimize_disk(self):
        print("Optimizing disk by defragmentation...")
        new_storage = [None] * self.disk_size
        new_bitmap = [0] * self.disk_size
        new_directory = {}
        next_free_block = 0

        for filename, (start, size) in self.directory.items():
            new_directory[filename] = (next_free_block, size)
            for i in range(size):
                new_storage[next_free_block] = self.storage[start + i]
                new_bitmap[next_free_block] = 1
                next_free_block += 1
        
        self.storage, self.bitmap, self.directory = new_storage, new_bitmap, new_directory
        print("Disk optimization complete. Files defragmented.")

# Example Usage
fs = FileSystem()
fs.create_file("file1", 5, "hello")
fs.read_file("file1")
fs.simulate_crash()
fs.recover_system()
fs.optimize_disk()
fs.read_file("file1")
