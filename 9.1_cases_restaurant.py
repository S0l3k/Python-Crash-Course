class Restaurant():
    """"Describe all restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """"Initializes attributes restaurant_name and cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """"Printing information about restaurant_name and cuisine_type"""
        print(f"\nRestaurant have name: {self.restaurant_name}.")
        print(f"Restaurant have a cuisine type: {self.cuisine_type}.")

    def open_restaurant(self):
        """"Printing 'restaurant open'"""
        print(f"\nOur restaurant '{self.restaurant_name}' is open!")

restaurant = Restaurant('Sqwoz bab', 't-type')

print(f"Restaurant name is {restaurant.restaurant_name}.")
print(f"Restaurant have a cuisine type {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()