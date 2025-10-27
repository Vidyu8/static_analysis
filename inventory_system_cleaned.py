""" 
Inventory Management System

This module provides functionality for managing inventory items,
including adding, removing, and tracking stock levels. 
"""
import json
import ast
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add items to inventory with logging.

    Args:
        item (str): Name of the item to add
        qty (int): Quantity to add
        logs (list, optional): List to store log messages

    Returns:
        list: Updated logs list
    """
    if logs is None:
        logs = []
    if not item:
        return logs

    if not isinstance(qty, (int, float)):
        raise ValueError("Quantity must be a number")

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    return logs


def remove_item(item, qty):
    """Remove items from inventory.

    Args:
        item (str): Name of the item to remove
        qty (int): Quantity to remove

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        if not isinstance(qty, (int, float)):
            raise ValueError("Quantity must be a number")

        if item not in stock_data:
            return False

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
        return True
    except KeyError:
        return False
    except ValueError as e:
        print(f"Error: {e}")
        return False


def get_qty(item):
    """Get quantity of specific item.

    Args:
        item (str): Name of the item

    Returns:
        int: Quantity of the item, 0 if not found
    """
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from JSON file.

    Args:
        file (str): Path to the JSON file

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(file, "r", encoding='utf-8') as file_handler:
            global stock_data
            stock_data = json.loads(file_handler.read())
        return True
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return False


def save_data(file="inventory.json"):
    """Save inventory data to JSON file.

    Args:
        file (str): Path to the JSON file

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(file, "w", encoding='utf-8') as file_handler:
            file_handler.write(json.dumps(stock_data, indent=2))
        return True
    except IOError as e:
        print(f"Error saving data: {e}")
        return False


def print_data():
    """Print all inventory items in a formatted way."""
    print("\n=== Inventory Report ===")
    if not stock_data:
        print("No items in inventory")
        return

    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")
    print("=======================\n")


def check_low_items(threshold=5):
    """Check for items below threshold quantity.

    Args:
        threshold (int): Minimum quantity threshold

    Returns:
        list: Items below the threshold
    """
    return [item for item, qty in stock_data.items() if qty < threshold]


def safe_eval_demo():
    """Demonstrate safe alternative to eval.

    Returns:
        None
    """
    user_input = '{"name": "test", "value": 42}'
    try:
        parsed_data = ast.literal_eval(user_input)
        print(f"Safe parsing result: {parsed_data}")
    except (ValueError, SyntaxError):
        print("Invalid input for safe parsing")


def main():
    """Main function to demonstrate inventory system functionality.

    Returns:
        None
    """
    logs = []

    add_item("apple", 10, logs)
    add_item("banana", 5, logs)

    try:
        add_item(123, "ten")  
    except ValueError as e:
        print(f"Caught expected error: {e}")

    remove_item("apple", 3)
    remove_item("orange", 1)  

    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items(8))

    print("\n=== Activity Log ===")
    for log in logs:
        print(log)

    save_data()
    load_data()
    print_data()

    safe_eval_demo()


if __name__ == "__main__":
    main()
    
