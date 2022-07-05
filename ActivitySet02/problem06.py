class Menu:
    """fill in class definition here"""
        
    def add(self,value,number):
        self.value=value
        self.number=number
    def show(self):
        print(self.value,self.number)

m = Menu()     # Menu is a class
m.add("idly", 10)
m.show()
m.add("vada", 20)
m.show()      
   