class dog: 
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
    def description(self):
        print (self.name)
    def get_info(self):
        print(self.color)
class JackRussellTerrier(dog):
    def name(self,Name):
        print(self.name)
    def age(self,Age):
        print(self.age)

class BullDog(dog):
     def name1(self,Name):
        print(self.name)
         
     def age1(self,Age):
        print(self.age)

Class=dog("rocky",10,"brown")
Class.description()
Class1=BullDog("rocky",10,"brown")
Class1.name1("bulldog")
print(Class1)