# #learning classes and objects
# #class players:
# #     cricket="have fun"
# #     def __init__(self,name,age) -> None:
# #         self.name=name
# #         self.age=age  
# #     def info(self):
# #         print(self.name ,"is", self.age,"years old and" ,self.cricket)
# #     def style(self,position):
# #         return f"{self.name} is {position}"
# #     def sty(self,position):
# #         return f"{self.name} at {position}"
# #     def __str__(self):
# #         return("you are a legend")
# # class classic(players):
# #     def style(self,position="toporder"):
# #         return super().sty(position)       
# # class powerhitter(players):
# #     def style(self,position="finishing"):
# #         return super().sty(position)
        

# # goat=classic('virat',33)
# # # goat.info()
# # # print(goat.style("toporder batsmen"))
# # print(goat.style())
# # print(goat)
# # captain=powerhitter('dhoni',40)
# # # captain.info()
# # print(captain.style())
# # print(captain)
# # print(type(goat))
# # print(type(captain))

# # m=tuple()
# # l=("hi",1)
# # b=("hey",2)
# # x=dict()
# # x=m+l+b
# # print(x)
# # x=dict()
# # x['k']=1
# # x['m']=2
# # print(x)
# class A:
#     def __init__(self, a):
#         self.a = a
 
#     # Overloading ~ operator, but with two operands
#     def __invert__(self, other):
#         return self.aother.a
 
 
# ob1 = A(2)
# ob2 = A(3)
# print(ob1+ob2)