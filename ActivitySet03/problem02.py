# x=['0.0 0.0 0.0 1.0 1.0 0.0', '-1.0 2.0 3.0 5.0 1.0 1.0', '5.0 9.0 -0.5 0.0 7.5 5.0']
# print(x[1][2])
from cmath import sqrt
def no_triangle():
    n=int(input("enter number of tiangles you want to input"))
    return n 
def xcoordinates(n):
    x1=list()
    x2=list()
    x3=list()
    for i in range(n):
        i=float(input('enter the x1 coordinates'))
        x1.append(i)
    for i in range(n):
        i=float(input('enter the x2 coordinates'))
        x2.append(i)
    for i in range(n):
        i=float(input('enter the x3 coordinates'))
        x3.append(i)
    return x1,x2,x3
def ycoordinates(n):
    y1=list()
    y2=list()
    y3=list()
    for i in range(n):
        i=float(input('Enter the y1 coordinates'))
        y1.append(i)
    for i in range(n):
        i=float(input('Enter the y2 coordinates'))
        y2.append(i)
    for i in range(n):
        i=float(input('Enter the y3 coordinates'))
        y3.append(i)
    return y1,y2,y3
def findarea(n,x1,x2,x3,y1,y2,y3):
    area=list()
    for i in range(n):
        print(i)
        ar=sqrt(float(x2[i])-float(x1[i]))*(float(x2[i])-float(x1[i]))-(float(y2[i])-float(y1[i]))*(float(y2[i])-float(y1[i]))*sqrt(float(x3[i])-float(x1[i]))*(float(x3[i])-float(x1[i]))-(float(y3[i])-float(y1[i]))*(float(y3[i])-float(y1[i]))
        print(ar)
        area.append(ar)
        return area
def main():
    n=no_triangle()
    x1,x2,x3=xcoordinates(n)
    y1,y2,y3=ycoordinates(n)
    area=findarea(n,x1,x2,x3,y1,y2,y3)
    print(x1,x2,x3,y1,y2,y3)
    print(y1)
    print(area)
    
if __name__ == '__main__':
    main()