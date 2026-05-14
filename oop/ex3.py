class User:
    def __init__(self, first_name, last_name, age, mobile_number, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.mobile_number = mobile_number
        self.country = country

    def describe_user(self):
        print(f"Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Mobile Number: {self.mobile_number}")
        print(f"Country: {self.country}")
        print()

    def greet_user(self):
        print(f"hello, {self.first_name} {self.last_name} wish u best luck")
        print()


user1 = User("Gela", "Barkalaia", "53", "595271932", "Georgia")
user2 = User("Mike", "Tyson", "55", "+37251232", "I Dont Know")
user3 = User("Giraffe", "Joze", "32", "572123252", "Georgia")


user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()