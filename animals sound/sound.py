animals=input("Which animal would you like to know about?")
class Animal():
    def __init__(self,name,species,habitat):
        self.name=name
        self.species=species
        self.habitat=habitat
    # def make_sound(self):
    #     print("Animals sound")
class Lion(Animal):
    def __init__(self, name, species, habitat):
        super().__init__(name, species, habitat)
    # def make_sound(self):
    #     return super().make_sound()
    def details(self):
        print(f"{self.name} is a {self.species}. It lives on {self.habitat}")
class Dog(Animal):
    def __init__(self, name, species, habitat):
        super().__init__(name, species, habitat)
    # def make_sound(self):
    #     return super().make_sound()
    def details(self):
        print(f"{self.name} is a {self.species}. It lives on {self.habitat}") 
if animals=="lion":              
    lion_object=Lion("Lion","MAMMAL","lAND")
    lion_object.details()
    print("Lion roars")

elif animals=="dog":
    dog_object=Dog("Dog","Mammal","Land")
    dog_object.details()
    print("Dog barks Woof woof!")

