# Base Animal class (for reference)
class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} makes a sound: {self.sound}")

# Modified Dog class
class Dog(Animal):
    def __init__(self, name, age, breed):
        self.breed = breed  # Initialize the new breed attribute
        super().__init__(name, age, "Woof")  # Call Animal constructor

    def make_sound(self):
        print(f"{self.name} says: Woof!")

    def show_breed(self):
        print(f"{self.name} is a {self.breed}.")

# Create a new Dog instance
dog2 = Dog("Buddy", 4, "Golden Retriever")

# Call methods
dog2.make_sound()
dog2.show_breed()
