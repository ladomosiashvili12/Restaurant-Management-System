"""
Main entry point for Restaurant Management System
Run this file to start the application
"""

from backend.backend import get_restaurant_data, get_menu
from frontend.frontend import display_dashboard, display_menu, process_order, make_reservation


def main():
    """Main application function"""
    print("\n" + "🍽️  WELCOME TO RESTAURANT MANAGEMENT SYSTEM 🍽️")
    
    # Display dashboard
    display_dashboard()
    
    # Display menu
    display_menu()
    
    # Example: Process an order
    print("Processing a sample order...")
    order_data = {"items": ["Pasta", "Salad"], "table": 3}
    process_order(order_data)
    
    # Example: Make a reservation
    print("\nMaking a sample reservation...")
    make_reservation(guests=4, time="19:00")
    
    print("\n✅ All systems operational!")


if __name__ == "__main__":
    main()
