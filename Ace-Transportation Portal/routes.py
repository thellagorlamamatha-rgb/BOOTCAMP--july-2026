# routes.py

# -----------------------------------------
# 1. LIST - Bus stops for Route 1
# (Ordered collection, can be modified)

route_1_stops = ["College Gate", "RTC Cross", "Miyapur"]

# -----------------------------------------
# 2. TUPLE - GPS Coordinates of each stop
# (Fixed data, immutable)

stop_coordinates = (17.4939, 78.3996)

# -----------------------------------------
# 3. SET - Registered Student Pass IDs
# (Unique values only, no duplicates)

registered_pass_ids = {"ACE001", "ACE002", "ACE003"}

# -----------------------------------------
# 4. DICTIONARY - Bus Fleet Details
# (Key-Value structured data)

bus_fleet = {
    "bus_no": "AP28Z1234",
    "capacity": 50,
    "driver": "Ramesh"
}

# -----------------------------------------
# Display all stops for a given route

def display_route_stops(route_stops):
    print("\nRoute Stops:")
    for stop in route_stops:
        print(stop)

# -----------------------------------------
# Add a new stop to an existing route

def add_stop(route_stops, new_stop):
    route_stops.append(new_stop)
    print(f"{new_stop} added successfully.")

# -----------------------------------------
# Register a new student pass ID

def register_student_pass(pass_set, student_id):
    if student_id not in pass_set:
        pass_set.add(student_id)
        print(f"{student_id} registered successfully.")
    else:
        print("Student ID already exists.")

# -----------------------------------------
# Display all bus fleet details

def display_bus_details(bus_dict):
    print("\nBus Details:")
    for key, value in bus_dict.items():
        print(f"{key}: {value}")


