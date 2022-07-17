# from cmath import sqrt


# def no_triangle():
#     n=int(input("enter number of tiangles you want to input"))
#     return n 
# def xcoordinates(n):
#     x1=list()
#     x2=list()
#     x3=list()
#     for i in range(n):
#         i=float(input('enter the x1 coordinates'))
#         x1.append(i)
#     for i in range(n):
#         i=float(input('enter the x2 coordinates'))
#         x2.append(i)
#     for i in range(n):
#         i=float(input('enter the x3 coordinates'))
#         x3.append(i)
#     return x1,x2,x3
# def ycoordinates(n):
#     y1=list()
#     y2=list()
#     y3=list()
#     for i in range(n):
#         i=float(input('Enter the y1 coordinates'))
#         y1.append(i)
#     for i in range(n):
#         i=float(input('Enter the y2 coordinates'))
#         y2.append(i)
#     for i in range(n):
#         i=float(input('Enter the y3 coordinates'))
#         y3.append(i)
#     return y1,y2,y3
# def findarea(n,x1,x2,x3,y1,y2,y3):
#     area=list()
#     for i in range(n):
#         ar=sqrt((x2[i]-x1[i])*(x2[i]-x1[i])-(y2[i]-y1[i]))*(y2[i]-y1[i])*sqrt((x3[i]-x1[i])*(x3[i]-x1[i])-(y3[i]-y1[i])*(y3[i]-y1[i]))
#         area.append(ar)
#         return area
# def main():
#     n=no_triangle()
#     x1,x2,x3=xcoordinates(n)
#     y1,y2,y3=ycoordinates(n)
#     area=findarea(n,x1,x2,x3,y1,y2,y3)
#     print(area)
   
def no_rectangle():
    n=int(input("enter number of tiangles you want to input"))
    return n
def input_coordinates(n):
    xy=list()
    for i in range(n):
        i=(input('enter the coordinates'))
        i.split(' ')
        xy.append(i)
    return xy
def findarea(n,xy):
    for i in n:
        for j in xy:
            ug
def main():
    n=no_rectangle()
    print(n)
    xy=input_coordinates(n)
    print(xy)
if __name__ == '__main__':
    main()         
      