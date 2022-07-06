class Menu:
    """fill in class definition here"""
    def __init__(self):
        self=self
    def add(self,value,number):
        x=dict()
        y=dict()
        
        self.y=y
        self.value=value
        self.number=number
        self.x=x
        self.x={self.value:self.number}

    def __add__(self,other):
       
        self.y=Menu({**self.x,**other.x})
        print(self.y)

    def show(self):
        for i in self.y:
            print(i,self.y[i])
        

m = Menu()     # Menu is a class
m.add("idly", 10)
m.add("vada", 20)
m.show()      