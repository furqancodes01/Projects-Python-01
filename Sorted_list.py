import bisect

class SortedList:
    def __init__(self):
        self.lst = []
        
    def add(self,value):
        bisect.insort(self.lst,value)
    
    def remove(self,value):
        self.lst.remove(value)
    
    def search(self , key):
        return self.lst.index(key)
    
    def insert_position(self , value):
        position = bisect.bisect_left(self.lst , value)
        return position

    def display(self):
        print(self.lst)

sl = SortedList()
sl.add(10)
sl.add(5)
sl.add(7)
sl.add(8)
sl.add(9)
sl.remove(7)
index = sl.insert_position(6)
print(index)
check = sl.display()