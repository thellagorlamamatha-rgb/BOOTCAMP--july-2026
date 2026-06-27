class Vehicle:
    # Class Variables
    college_name = "ACE Engineering College"
    total_vehicles = 0

    def __init__(self, vehicle_id, vehicle_type, capacity):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.capacity = capacity

        Vehicle.total_vehicles += 1

    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles

    @staticmethod
    def validate_vehicle_id(vehicle_id):
        return vehicle_id.startswith("AP") and len(vehicle_id) >= 8

    def display_info(self):
        print("College :", Vehicle.college_name)
        print("Vehicle ID :", self.vehicle_id)
        print("Vehicle Type :", self.vehicle_type)
        print("Capacity :", self.capacity)


class Bus(Vehicle):

    def __init__(self, vehicle_id, capacity, route_number, has_ac=False):
        super().__init__(vehicle_id, "Bus", capacity)
        self.route_number = route_number
        self.has_ac = has_ac

    def __str__(self):
        ac = "Yes" if self.has_ac else "No"
        return f"Bus {self.vehicle_id} | Route:{self.route_number} | Capacity:{self.capacity} | AC:{ac}"

    def __repr__(self):
        return f"Bus(vehicle_id='{self.vehicle_id}', route='{self.route_number}', capacity={self.capacity})"

    def display_info(self):
        super().display_info()
        print("Route Number :", self.route_number)
        print("AC :", self.has_ac)


class MiniVan(Vehicle):

    def __init__(self, vehicle_id, capacity, trip_purpose):
        super().__init__(vehicle_id, "MiniVan", capacity)
        self.trip_purpose = trip_purpose

    def __str__(self):
        return f"MiniVan {self.vehicle_id} | Capacity:{self.capacity} | Purpose:{self.trip_purpose}"

    def __repr__(self):
        return f"MiniVan(vehicle_id='{self.vehicle_id}', purpose='{self.trip_purpose}')"

    def display_info(self):
        super().display_info()
        print("Trip Purpose :", self.trip_purpose)


