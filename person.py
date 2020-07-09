class Person(object):
    #constructor
    def __init__(self, name, age):
        print("Person Instantiated")
        self.Name = name
        self.Age = age
    
    def saysHello(self):
        print(f"{self.Name} says Hello!")




person = Person("Tom", 30)
person.saysHello()
