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

restaurant_1 = Restaurant('Alividerchi', 'c-type')
restaurant_2 = Restaurant('Chao-Kakao', 'u-type')
restaurant_3 = Restaurant('Girl, are you down! ahahaha', 'quadre')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()