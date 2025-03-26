import unittest
from main import FileSystem  

class TestFileSystem(unittest.TestCase):
    
    def setUp(self):
        self.fs = FileSystem()
    
    def test_create_file(self):
        self.fs.create_file("file1", "hello")
        self.assertIn("file1", self.fs.directory)
    
    def test_read_file(self):
        self.fs.create_file("file1", "hello")
        self.assertEqual(self.fs.read_file("file1"), "hello")
    
    def test_delete_file(self):
        self.fs.create_file("file1", "hello")
        self.fs.delete_file("file1")
        self.assertNotIn("file1", self.fs.directory)
    
    def test_defragment(self):
        self.fs.create_file("file1", "hello")
        self.fs.create_file("file2", "world")
        self.fs.defragment()
        self.assertEqual(set(self.fs.directory.keys()), {"file1", "file2"})
    
    def test_backup_and_restore(self):
        self.fs.create_file("file1", "hello")
        self.fs.backup_system()
        new_fs = FileSystem()
        new_fs.restore_system()
        self.assertIn("file1", new_fs.directory)
    
if __name__ == "__main__":
    unittest.main()
