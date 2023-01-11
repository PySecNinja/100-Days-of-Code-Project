#See how cat and dog class inherate the pet class functions

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} old.")
    
    def speak(self):
        print("I dont know what to say")
    

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)     #super references parent class pet
        self.color = color

    def speak(self):
        print("Meow")
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} old and I am {self.color}")        
        
class Dog(Pet):
        
    def speak(self):
        print("Bark")
        
class Fish(Pet):
    pass
        
# variable_1 = input("What is your name?")
# variable_2 = input("How old are you?")
# p = Pet(variable_1, variable_2)


# cat and dog are defined in child class so that takes precedence 
p = Pet("Tim", 19)
p.speak()
c = Cat("Bill", 34, "Brown")
c.show()
c.speak()
d = Dog("Jill", 25)
d.speak()
f = Fish("Bubbles", 10)
f.speak()

