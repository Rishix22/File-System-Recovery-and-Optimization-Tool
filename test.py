import unittest
from main import FileSystem  

class TestFileSystem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up a single FileSystem instance for testing."""
        cls.fs = FileSystem()

    def tearDown(self):
        """Reset the FileSystem after each test to ensure independence."""
        self.fs = FileSystem()

    def test_create_file(self):
        self.fs.create_file("file1", "hello")
        self.assertIn("file1", self.fs.directory, "File was not created properly.")

    def test_read_file(self):
        self.fs.create_file("file1", "hello")
        self.assertEqual(self.fs.read_file("file1"), "hello", "File content mismatch.")

    def test_delete_file(self):
        self.fs.create_file("file1", "hello")
        self.fs.delete_file("file1")
        self.assertNotIn("file1", self.fs.directory, "File deletion failed.")

    def test_defragment(self):
        self.fs.create_file("file1", "hello")
        self.fs.create_file("file2", "world")
        self.fs.defragment()
        self.assertEqual(set(self.fs.directory.keys()), {"file1", "file2"}, "Defragmentation error.")

    def test_backup_and_restore(self):
        self.fs.create_file("file1", "hello")
        self.fs.backup_system()

        # Restore in a new instance to verify persistence
        restored_fs = FileSystem()
        restored_fs.restore_system()

        self.assertIn("file1", restored_fs.directory, "Backup & restore failed.")

if __name__ == "__main__":
    unittest.main()
