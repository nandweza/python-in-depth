def greet():
    print("Hello,")
    print("World!")
    print("How is the eclipse...")

greet()


def greet_with_name(name):
    print(f"Hello, {name}")
    print(f"How are you doing, {name}")

greet_with_name("Allan")


def name_with_location(name, location):
    print(f"Hello, {name} from {location}")

name_with_location("James", "Boise")

#Functions with keyword argument
name_with_location(name="Joe", location="San diego")