def add(a, b):
  c=a+b
  print(c)
  return c


def main():
  a = float(input('Enter the number')) 
  b = float(input('Enter the number')) 

  c = add(a,b)
  
  print(c)
if __name__ == '__main__':
    main()

