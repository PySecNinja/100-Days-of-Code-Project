class Animal:
    def __init__(self):                     # This is an attribute
        self.num_eyes = 2
        
    def breathe(self):                      # This is a method
        print("Inhale, exhale")

class Fish(Animal):                         # Fish class will inherit the attribute and method of animal class
    def __init__(self):
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("doing this underwater")
    
    def swim(self):
        print("moving in water.")
        
nemo = Fish()
nemo.swim()
nemo.breathe()                              # If we didn't add like 8-10 we couldn't call the breathe method
print(nemo.num_eyes)