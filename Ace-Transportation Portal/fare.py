from abc import ABC, abstractmethod

# ==========================================
# ABSTRACT BASE CLASS
# ==========================================
class FareCalculator(ABC):
    """
    NOTE: This class cannot be instantiated directly.
    It forces all subclasses to implement required methods.
    """
    def __init__(self, student_id, distance_km):
        # TODO: Assign instance variables
        self.student_id = student_id
        self.distance_km = distance_km

    # ABSTRACT METHOD 1
    # Every subclass MUST override this method.
    # Purpose: Calculate and return the fare amount.
    @abstractmethod
    def calculate_fare(self):
        # Do NOT write any code here.
        pass

    # ABSTRACT METHOD 2
    # Every subclass MUST override this method.
    # Purpose: Print a formatted fare receipt.
    @abstractmethod
    def display_fare_summary(self):
        # Do NOT write any code here.
        pass

    # CONCRETE METHOD: shared by all subclasses.
    # TODO: Calculate discounted amount and return it.
    def apply_discount(self, amount, discount_percent):
        discounted_amount = amount - (amount * discount_percent / 100)
        return discounted_amount


# ==========================================
# CONCRETE SUBCLASSES (Required Implementation)
# ==========================================

class RouteFare(FareCalculator):
    """Concrete Class for Regular Route passes"""
    def __init__(self, student_id, distance_km, base_rate=15):
        super().__init__(student_id, distance_km)
        self.base_rate = base_rate

    def calculate_fare(self):
        # Example calculation: distance multiplied by a base rate
        return self.distance_km * self.base_rate

    def display_fare_summary(self):
        fare = self.calculate_fare()
        print("\n--- Route Fare Receipt ---")
        print(f"Student ID : {self.student_id}")
        print(f"Distance   : {self.distance_km} km")
        print(f"Total Fare : ${fare:.2f}")


class SpecialTripFare(FareCalculator):
    """Concrete Class for Special Trip bookings"""
    def __init__(self, student_id, distance_km, flat_charge=50, rate_per_km=20):
        super().__init__(student_id, distance_km)
        self.flat_charge = flat_charge
        self.rate_per_km = rate_per_km

    def calculate_fare(self):
        # Example calculation: flat booking charge + distance rate
        return self.flat_charge + (self.distance_km * self.rate_per_km)

    def display_fare_summary(self):
        fare = self.calculate_fare()
        # Example using the shared concrete method for a 10% holiday discount
        discounted = self.apply_discount(fare, 10)
        print("\n--- Special Trip Receipt ---")
        print(f"Student ID      : {self.student_id}")
        print(f"Distance        : {self.distance_km} km")
        print(f"Standard Fare   : ${fare:.2f}")
        print(f"Discounted Fare : ${discounted:.2f} (10% Off)")


# ==========================================
# VERIFICATION / EXECUTION
# ==========================================
if __name__ == "__main__":
    # 1. Test Regular Route Pass
    route_pass = RouteFare(student_id="ACE101", distance_km=25)
    route_pass.display_fare_summary()

    # 2. Test Special Trip Booking
    special_trip = SpecialTripFare(student_id="ACE202", distance_km=40)
    special_trip.display_fare_summary()