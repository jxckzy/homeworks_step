class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = 100

    def sleep(self, hours):
        self.energy += hours * 10
        print(f"{self.name} is sleeping for {hours} hours.")

    def make_sound(self):
        pass


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        self.hunger = 0

    def play(self, minutes):
        if self.energy >= minutes * 5:
            self.energy -= minutes * 5
            self.hunger += minutes * 2
            print(f"{self.name} is playing for {minutes} minutes.")
        else:
            print(f"{self.name} is too tired to play.")

    def make_sound(self):
        print(f"{self.name} says: Meow!")


if __name__ == "__main__":
    my_cat = Cat("Masik", 3, "Ginger")
    print(f'Hello, this is my {my_cat.name} and it is {my_cat.age} years old. He is {my_cat.color} by the color')
    my_cat.sleep(8)
    my_cat.play(15)
    my_cat.make_sound()