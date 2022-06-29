def input_two_numbers():
    a=float(input('Enter the first number'))
    b=float(input('Enter the second number'))
    return a,b

def add(a, b):
    sum=a+b
    return sum


def output(a, b, sum):
    print('the sum of',a,b,'is',sum)


def main():
    a, b = input_two_numbers()
    sum = add(a, b)

    output(a, b, sum)



if __name__ == '__main__':
    main()
