# transport_manager.py

from vehicles import Bus, MiniVan
from drivers import Driver

class TransportManager:
    def __init__(self, manager_name):
        # Public instance variable
        self.manager_name = manager_name
        
        # COMPOSITION
        # TransportManager "has" lists of other objects
        # TODO: Initialize these empty lists below
        self.buses = []        # List of Bus objects
        self.mini_vans = []    # List of MiniVan objects
        self.drivers = []      # List of Driver objects

    # -------------------------------------------------------------
    # TODO: Add a Bus object to self.buses
    # Hint: Use append() function. Make sure to validate first!
    def add_bus(self, bus_obj):
        if isinstance(bus_obj, Bus):
            self.buses.append(bus_obj)
        else:
            print("Invalid object type! Expected a Bus instance.")

    # -------------------------------------------------------------
    # TODO: Add a MiniVan object to self.mini_vans
    # Hint: Use append() function. Remember to validate!
    def add_minivan(self, van_obj):
        if isinstance(van_obj, MiniVan):
            self.mini_vans.append(van_obj)
        else:
            print("Invalid object type! Expected a MiniVan instance.")

    # -------------------------------------------------------------
    # TODO: Add a Driver object to self.drivers
    # Hint: Use append() function. Driver object validation is optional.
    def add_driver(self, driver_obj):
        if isinstance(driver_obj, Driver):
            self.drivers.append(driver_obj)
        else:
            print("Invalid object type! Expected a Driver instance.")

    # -------------------------------------------------------------
    # POLYMORPHISM
    # TODO: Combine both lists and call same name method
    # 1. Loop through all objects in the combined list
    # 2. Inside loop, call display_info() method
    # Hint: Two distinct objects (Bus and MiniVan) display_info()
    #       will produce DIFFERENT outputs ... that is Polymorphism
    def display_all_vehicles(self):
        # Combine lists of both vehicle types
        all_vehicles = self.buses + self.mini_vans
        
        if not all_vehicles:
            print("No vehicles registered under this manager.")
            return

        # Polymorphic method call
        for vehicle in all_vehicles:
            vehicle.display_info()
