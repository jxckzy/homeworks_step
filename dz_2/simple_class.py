class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 0
        self.energy = 100

    def meow(self):
        print(f"{self.name} says: Meow!")

    def sleep(self, hours):
        self.energy += hours * 10
        print(f"{self.name} is sleeping for {hours} hours.")

    def play(self, minutes):
        if self.energy >= minutes * 5:
            self.energy -= minutes * 5
            self.hunger += minutes * 2
            print(f"{self.name} is playing for {minutes} minutes.")
        else:
            print(f"{self.name} is tired.")

    def eat(self, food):
        if self.hunger >= food:
            self.hunger -= food
            print(f"{self.name} is eating.")
        else:
            print(f"{self.name} is hungry.")


if __name__ == "__main__":
    my_cat = Cat("Masik", 3)
    my_cat.meow()
    my_cat.sleep(8)
    my_cat.play(15)
    my_cat.eat(10)