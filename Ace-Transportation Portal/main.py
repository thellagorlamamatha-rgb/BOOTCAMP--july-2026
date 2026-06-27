from transport_manager import TransportManager
from vehicles import Bus, MiniVan
from drivers import Driver


def display_main_menu():
    """Prints the console dashboard interface."""
    print("\n" + "=" * 55)
    print("      ACE Engineering College Transportation Portal      ")
    print("=" * 55)
    print("1. Add New Vehicle")
    print("2. Add New Driver")
    print("3. View All Vehicles & Drivers")
    print("4. Search for a Vehicle")
    print("5. View Portal Dashboard Summary")
    print("6. Exit Application")
    print("=" * 55)


def get_valid_input(prompt):
    """Helper to ensure clean, non-empty text input."""
    while True:
        try:
            value = input(prompt).strip()
            if value:
                return value
            print("Input cannot be empty. Please try again.")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting program...")
            exit()


def main():
    manager = TransportManager("ACE Engineering College")

    print("Initializing ACE Transportation Portal System...")

    while True:
        display_main_menu()

        try:
            choice = input("Enter your choice (1-6): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nThank you for using ACE Transportation Portal.")
            break

        if choice == "1":
            print("\n--- Add New Vehicle ---")

            v_type = get_valid_input("Enter Vehicle Type (Bus/MiniVan): ").lower()
            v_id = get_valid_input("Enter Vehicle ID: ")
            v_name = get_valid_input("Enter Vehicle Name/Route: ")

            if v_type == "bus":
                vehicle = Bus(v_id, v_name)
                manager.add_vehicle(vehicle)
                print(f"Bus '{v_id}' added successfully.")

            elif v_type in ("minivan", "mini van"):
                vehicle = MiniVan(v_id, v_name)
                manager.add_vehicle(vehicle)
                print(f"MiniVan '{v_id}' added successfully.")

            else:
                print("Invalid vehicle type! Please enter Bus or MiniVan.")

        elif choice == "2":
            print("\n--- Add New Driver ---")

            d_id = get_valid_input("Enter Driver ID: ")
            d_name = get_valid_input("Enter Driver Name: ")

            driver = Driver(d_id, d_name)
            manager.add_driver(driver)

            print(f"Driver '{d_name}' registered successfully.")

        elif choice == "3":
            print("\n--- Registered Vehicles & Drivers ---")

            # Display all vehicles if method exists
            if hasattr(manager, "display_all_vehicles"):
                manager.display_all_vehicles()

            # Display all drivers if method exists
            if hasattr(manager, "display_all_drivers"):
                manager.display_all_drivers()

        elif choice == "4":
            print("\n--- Search Vehicle ---")

            search_id = get_valid_input("Enter Vehicle ID: ")

            if hasattr(manager, "search_vehicle"):
                manager.search_vehicle(search_id)
            else:
                print("Search feature is not implemented.")

        elif choice == "5":
            print("\n--- Dashboard Summary ---")

            if hasattr(manager, "display_dashboard"):
                manager.display_dashboard()
            else:
                print("Dashboard feature is not implemented.")

        elif choice == "6":
            print("\nThank you for using ACE Transportation Portal.")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
        print("Thank you for using ACE Transportation Portal.")