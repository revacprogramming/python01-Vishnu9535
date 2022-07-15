class Menu:
    """fill in class definition here"""
    def __init__(self):
        self.k=dict()
    def __setitem__(self,a,b):
        self.k[a]=b
    def __str__(self):
        return self.k.__str__()
    

m = Menu() 
m["idly"] = 10
m["vada"] = 20
print(m)