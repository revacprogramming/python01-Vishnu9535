def no_of_instances():
    x=int(input('enter nunmber of instances'))
    return x
def sum_of_unitfractions(x):
    m=list()
    for i in range(x):
        num=0
        den=1
        no=(input('enter number fraction to be summed'))
        input_numbers=(input('enter the number'))
        m=input_numbers.split(" ")
        for j in m:
            num=num*int(j)+1*int(den)
            den=int(j)*int(den)
        for k in range(x):
            for i in range(2,(int(den)+1)):
                if num%i==0 and den%i==0:
                    num=num/i
                    den=den/i
                continue
        print(num,"/",den)          
def main():
    x=no_of_instances()
    sum_of_unitfractions(x)    
if __name__ == '__main__':
    main()      