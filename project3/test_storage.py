"""
Unit tests for Project 3: To-Do List Application - Storage Module
"""

import unittest
import os
from todo import ToDoList, Task
from storage import save_tasks, load_tasks


class TestStorage(unittest.TestCase):
    """Test cases for storage functions."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_filename = "test_tasks.json"
    
    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
    
    def test_save_tasks(self):
        """Test saving tasks to a file."""
        # TODO: Implement this test
        pass
    
    def test_load_tasks(self):
        """Test loading tasks from a file."""
        # TODO: Implement this test
        pass
    
    def test_save_and_load_roundtrip(self):
        """Test saving and then loading tasks."""
        # TODO: Implement this test
        pass


if __name__ == "__main__":
    unittest.main()
