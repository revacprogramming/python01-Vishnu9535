

class Menu:
    """fill in class definition here"""


m = Menu()
m = m + ("idly", 10) + ("vada", 20)  # Hint: operator overloading special methods (__add__, __sub__, etc.)
    
print(m)  # should print the menu properly

#learning classes and objects
#class players:
#     cricket="have fun"
#     def __init__(self,name,age) -> None:
#         self.name=name
#         self.age=age  
#     def info(self):
#         print(self.name ,"is", self.age,"years old and" ,self.cricket)
#     def style(self,position):
#         return f"{self.name} is {position}"
#     def sty(self,position):
#         return f"{self.name} at {position}"
#     def __str__(self):
#         return("you are a legend")
# class classic(players):
#     def style(self,position="toporder"):
#         return super().sty(position)       
# class powerhitter(players):
#     def style(self,position="finishing"):
#         return super().sty(position)
        

# goat=classic('virat',33)
# # goat.info()
# # print(goat.style("toporder batsmen"))
# print(goat.style())
# print(goat)
# captain=powerhitter('dhoni',40)
# # captain.info()
# print(captain.style())
# print(captain)
# print(type(goat))
# print(type(captain))


