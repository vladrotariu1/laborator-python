class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def make_sound(self):
        pass

    def move(self):
        print(f"{self.name} moves.")


class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} makes a mammal sound.")

    def give_birth(self):
        print(f"{self.name} gives birth to live young.")


class Bird(Animal):
    def __init__(self, name, habitat, feather_color):
        super().__init__(name, habitat)
        self.feather_color = feather_color

    def make_sound(self):
        print(f"{self.name} sings or chirps.")

    def lay_eggs(self):
        print(f"{self.name} lays eggs.")


class Fish(Animal):
    def __init__(self, name, habitat, scale_color):
        super().__init__(name, habitat)
        self.scale_color = scale_color

    def make_sound(self):
        print(f"{self.name} makes underwater sounds.")

    def lay_eggs(self):
        print(f"{self.name} lays eggs in the water.")


def main():
    lion = Mammal("Lion", "Grasslands", "Golden")
    lion.move()
    lion.make_sound()
    lion.give_birth()

    parrot = Bird("Parrot", "Rainforest", "Colorful")
    parrot.move()
    parrot.make_sound()
    parrot.lay_eggs()

    salmon = Fish("Salmon", "Freshwater", "Silver")
    salmon.move()
    salmon.make_sound()
    salmon.lay_eggs()


if __name__ == "__main__":
    main()
