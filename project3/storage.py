"""
Project 3: To-Do List Application - Storage Module
Student Name: [Your Name Here]
Date: [Date]
"""

import json


def save_tasks(todo_list, filename="tasks.json"):
    """
    TODO: Save tasks to a JSON file.
    
    Args:
        todo_list (ToDoList): The to-do list to save
        filename (str): The file to save to
    """
    # Your code here
    # Hint: Convert tasks to a list of dictionaries, then use json.dump()
    pass


def load_tasks(filename="tasks.json"):
    """
    TODO: Load tasks from a JSON file.
    
    Args:
        filename (str): The file to load from
    
    Returns:
        ToDoList: A ToDoList object with loaded tasks
    """
    # Your code here
    # Hint: Use json.load() and create Task objects from the data
    pass
