class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """


class Car: 
 # Constructor to initialize attributes
    def __init__(self, make, model, year):
        self.make = Toyota      # car's brand
        self.model = Corolla    # car's model 
        self.year = 2020      # year

    # Display car information
    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020
