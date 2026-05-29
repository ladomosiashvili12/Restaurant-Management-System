"""
Backend module for Restaurant Management System
This module contains all backend logic and functions
"""

def get_restaurant_data():
    """
    Get restaurant information
    Returns: dict with restaurant details
    """
    return {
        "name": "My Restaurant",
        "tables": 10,
        "staff": 5,
        "status": "open"
    }


def add_order(order_data):
    """
    Process a new order
    Args:
        order_data: dict containing order information
    Returns: dict with order status and ID
    """
    return {
        "status": "success",
        "order_id": 123,
        "message": "Order added successfully"
    }


def get_menu():
    """
    Get restaurant menu
    Returns: dict with menu items
    """
    return {
        "appetizers": ["Salad", "Soup"],
        "mains": ["Pasta", "Grilled Fish"],
        "desserts": ["Cake", "Ice Cream"]
    }


def reserve_table(guests, time):
    """
    Reserve a table
    Args:
        guests: int - number of guests
        time: str - reservation time
    Returns: dict with reservation details
    """
    return {
        "status": "confirmed",
        "table_number": 5,
        "guests": guests,
        "time": time
    }
