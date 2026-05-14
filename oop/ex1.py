class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def descirbe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cusine Type: {self.cuisine_type}")


    def open_restaurant(self):
        print(f"{self.restaurant_name} is already open")



restaurant = Restaurant("Qartuli Saxli", "Samegrelo")


print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.descirbe_restaurant()
restaurant.open_restaurant()
