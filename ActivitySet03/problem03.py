# x=['a','b','c','d']
# for j in range(len(x)):
#     print(x[j])

def number_of_strings():
    n=int(input('enter number of strings'))
    return n 
def input_string():
    words=list()
    no_letters=int(input('enter number of letters'))
    string=str(input('enter the of string'))
    print(string)

    def split(string):
        return list(char for char in string)
    words=split(string)
    return words,no_letters
def find_palindrome(words,no_letters):
    word3=''
    a=3
    k=0
    for z in range(no_letters):
        for i in range(k,no_letters):
            word3=word3+words[i]
            if len(word3)==a:
                a=a+1
                if word3==word3[::-1]:
                    print(k+1,word3)
        k=k+1
        word3=''
        a=3
def main():
    n=number_of_strings()
    for i in range(n):
        words,no_letters=input_string()
        find_palindrome(words,no_letters)
if __name__ == '__main__':
    main() 
    