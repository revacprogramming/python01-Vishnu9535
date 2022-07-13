class Menu:
    """fill in class definition here"""
    def __init__(self):
        self.k=tuple()
        
    def __add__(self,other):
        self.x=self.k+other
        return (self.x)     


m = Menu()
m = m + ("idly", 10) + ("vada", 20)  # Hint: operator overloading special methods (__add__, __sub__, etc.)
k=list()
for i in m:
    print(i)
print(m)  # should print the menu properly