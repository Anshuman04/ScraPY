class Animal:
    def __init__(self, legs):
        self.legs = legs
        self.can_walk = False
        self.can_swim = False
        self.can_fly = False

    def walk(self):
        if self.can_walk:
            print(f"I am walking with {self.legs} legs")
        else:
            print("I cannot walk")
    
    def swim(self):
        if self.can_swim:
            print("I am swimming")
        else:
            print("I cannot swim")

class Dog(Animal):
    def __init__(self, breed):
        super().__init__(4)
        self.can_walk = True
        self.can_swim = True
        self.breed = breed

class Spider(Animal):
    def __init__(self, pet_name):
        super().__init__(8)
        self.can_walk = True
        self.pet_name = pet_name

class Shark(Animal):
    def __init__(self, pet_name):
        super().__init__(0)
        self.can_swim = True
        self.pet_name = pet_name

class Alien(Animal):
    def __init__(self, pet_name):
        super().__init__(2)
        self.can_walk = True
        self.pet_name = pet_name

dog = Dog("Labrador")
spider = Spider("Spiderman")
shark = Shark("Sharky")

print("===== Playing with dog ======")
dog.walk()
dog.swim()
print("===== Playing with spider ======")
spider.walk()
spider.swim()
print("===== Playing with shark ======")
shark.walk()
shark.swim()
        
    