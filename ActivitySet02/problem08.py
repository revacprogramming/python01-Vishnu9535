

class Menu:
    """fill in class definition here"""
    def __init__(self):
        self.k=dict()
    def __add__(self,other):
        self.d=dict()
        return{**self.k,**other}


m = Menu()
m["idly"] = 10
m["vada"] = 20

print(m)
