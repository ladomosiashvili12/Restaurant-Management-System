"""
Frontend module for Restaurant Management System
This module contains all frontend logic and display functions
"""

import sys
from pathlib import Path

# Add parent directory to path to import backend
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.backend import get_restaurant_data, add_order, get_menu, reserve_table


def display_dashboard():
    """Display the main dashboard"""
    data = get_restaurant_data()
    print("\n" + "="*50)
    print("RESTAURANT DASHBOARD")
    print("="*50)
    print(f"Restaurant: {data['name']}")
    print(f"Tables: {data['tables']}")
    print(f"Staff: {data['staff']}")
    print(f"Status: {data['status']}")
    print("="*50 + "\n")
    return data


def display_menu():
    """Display the restaurant menu"""
    menu = get_menu()
    print("\n" + "="*50)
    print("MENU")
    print("="*50)
    for category, items in menu.items():
        print(f"\n{category.upper()}:")
        for item in items:
            print(f"  - {item}")
    print("\n" + "="*50 + "\n")
    return menu


def process_order(order_data):
    """Process an order through backend"""
    result = add_order(order_data)
    print(f"Order Result: {result}")
    return result


def make_reservation(guests, time):
    """Make a table reservation"""
    result = reserve_table(guests, time)
    print(f"Reservation: Table {result['table_number']} for {result['guests']} guests at {result['time']}")
    return result
