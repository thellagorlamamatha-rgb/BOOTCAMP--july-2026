class Driver:

    def __init__(self, driver_id, name, license_number, contact):
        self.driver_id = driver_id
        self.name = name
        self.license_number = license_number
        self.contact = contact

    # Getter for license_number
    @property
    def license_number(self):
        return self.__license_number

    # Setter for license_number
    @license_number.setter
    def license_number(self, value):
        if len(value) == 16:
            self.__license_number = value
        else:
            raise ValueError("License number must be exactly 16 characters.")

    # Getter for contact
    @property
    def contact(self):
        return self.__contact

    # Setter for contact
    @contact.setter
    def contact(self, value):
        if value.isdigit() and len(value) == 10:
            self.__contact = value
        else:
            raise ValueError("Contact number must contain exactly 10 digits.")

    # Deleter for contact
    @contact.deleter
    def contact(self):
        print("Deleting contact...")
        del self.__contact

    # Display method
    def display(self):
        print("Driver ID :", self.driver_id)
        print("Name :", self.name)
        print("License :", self.license_number)

        if hasattr(self, "_Driver__contact"):
            print("Contact :", self.contact)
        else:
            print("Contact : Deleted")


# Creating an object
d1 = Driver(
    driver_id=101,
    name="Rahul",
    license_number="DL12345678901234",   # 16 characters
    contact="9876543210"
)

