class Parent:
    def __init__(self,d):
        self.__data = d
        
    def show(self):
        print(self.__data)
        
class Child(Parent):
    
    def __init__(self, d):
        super().__init__(d)
        
    def display(self):
        print(self.__data)

c = Child(25)
c.show()
c.display()