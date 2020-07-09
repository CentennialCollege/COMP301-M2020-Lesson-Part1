class Person(object):
    #constructor
    def __init__(self, name, age):
        print("Person Instantiated")
        self.Name = name
        self.Age = age
    
    #method
    def saysHello(self):
        print(f"{self.Name} says Hello!")