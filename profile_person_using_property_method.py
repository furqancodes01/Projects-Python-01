from datetime import date


class Person:
    def __init__(self,fname,lname,year):
        self.__fname = fname
        self.__lname = lname
        self.year = year
    
    @property    
    def name (self):
        return f"{self.__fname} {self.__lname}"
    
    @name.setter
    def name(self,name):
        names = name.strip().split()
        if len(names) != 2:
            raise ValueError("Full name must include first and last name.")
        self.__fname,self.__lname = names
       
    @property
    def age(self):
        current_year = date.today().year
        return current_year - self.year
    
if __name__ == "__main__":
    p = Person("john","Doe",2000)
    
    print("Full Name:", p.name)
    print("Age:",p.age )