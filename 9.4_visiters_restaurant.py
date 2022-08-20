class Restaurant():
    """"Describe all restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """"Initializes attributes restaurant_name and cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """"Printing information about restaurant_name and cuisine_type"""
        print(f"\nRestaurant have name: {self.restaurant_name}.")
        print(f"Restaurant have a cuisine type: {self.cuisine_type}.")

    def open_restaurant(self):
        """"Printing 'restaurant open'"""
        print(f"\nOur restaurant '{self.restaurant_name}' is open!")

    def visitors(self):
        """Print number of visitors default"""
        print(f"Number of visitors: {self.number_served}")

    def set_number_served(self, number):
        """Changed number of visitors"""
        self.number_served = number
        print(f"Number of visitors, changed: {number}")

    def increment_number_served(self, number):
        """Increment 'number_served'"""
        self.number_served += number
        print(f"Number of visitors, increment: {self.number_served}")

restaurant = Restaurant('Sqwoz bab', 't-type')

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.visitors()

timursan = Restaurant('Ahahaha', 'dildo')

timursan.describe_restaurant()
timursan.set_number_served(5)
timursan.increment_number_served(15)