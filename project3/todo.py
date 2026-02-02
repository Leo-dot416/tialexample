"""
Project 3: To-Do List Application - Task Class
Student Name: [Your Name Here]
Date: [Date]
"""


class Task:
    """
    TODO: Implement a Task class to represent a single to-do item.
    
    Attributes:
        description (str): The task description
        completed (bool): Whether the task is completed
    """
    
    def __init__(self, description):
        """
        TODO: Initialize a new task.
        
        Args:
            description (str): The task description
        """
        # Your code here
        pass
    
    def mark_complete(self):
        """TODO: Mark this task as complete."""
        # Your code here
        pass
    
    def mark_incomplete(self):
        """TODO: Mark this task as incomplete."""
        # Your code here
        pass
    
    def __str__(self):
        """TODO: Return a string representation of the task."""
        # Your code here
        pass


class ToDoList:
    """
    TODO: Implement a ToDoList class to manage multiple tasks.
    
    Attributes:
        tasks (list): List of Task objects
    """
    
    def __init__(self):
        """TODO: Initialize an empty to-do list."""
        # Your code here
        pass
    
    def add_task(self, description):
        """
        TODO: Add a new task to the list.
        
        Args:
            description (str): The task description
        """
        # Your code here
        pass
    
    def remove_task(self, index):
        """
        TODO: Remove a task by index.
        
        Args:
            index (int): The index of the task to remove
        """
        # Your code here
        pass
    
    def get_all_tasks(self):
        """
        TODO: Get all tasks.
        
        Returns:
            list: List of all tasks
        """
        # Your code here
        pass
    
    def get_pending_tasks(self):
        """
        TODO: Get all incomplete tasks.
        
        Returns:
            list: List of incomplete tasks
        """
        # Your code here
        pass
