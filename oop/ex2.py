class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type        

    def describe_restaurant(self):
        print(f"Restaurant name {self.restaurant_name}")
        print(f"Cuisine type {self.cuisine_type}")
        print()

    def open_restaurant(self):
        print(f"{self.restaurant_name} is already open so you can visit")



restaurant1 = Restaurant("Georgian House", "Racha")
restaurant2 = Restaurant("Sushi Taste", "Japan")
restaurant3 = Restaurant("Lobiani", "Georgian")


restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()