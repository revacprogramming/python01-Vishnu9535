def seq_input():
    n=int(input('enter number of sequence to input'))
    return n
def inputsequence():
    noele=int(input('enter number of elements in the sequence'))
    sequence=(input('enter the sequence'))
    return noele,sequence
def run_sequence(noele,sequence):
    series=list()
    series=sequence.split(" ")
    seq=list()
    for i in series:
        seq.append(int(i))
    k=0
    x=noele
    try:
        for i in range(k,x):
            if seq[k]==0 and seq[k+1]!=0:
                for m in range(seq[k+1]):
                    print(seq[k+2],end=" ")
                k=k+3
                x=x-k
            elif seq[k]==0 and seq[k+1]==0:
                print(seq[k],end=" ")
                k=k+2
                x=x-k
            else:
                print(seq[k],end=" ")
                k=k+1
    except:
        print(" ")  
def main():
    n=seq_input()
    for i in range(n):
        noele,sequence=inputsequence()
        run_sequence(noele,sequence)
if __name__ == '__main__':
    main() 
# a=[1,0,2,0,0,10,1,2,3,4,0,3,0,2]
# k=0
# x=len(a)

# try:
#     for i in range(k,x):
#         if a[k]==0 and a[k+1]!=0 and a[k+2]!=0:
#             for j in range(a[k+1]):
#                 print(a[k+2],end=' ')
#             k=k+3
#             x=x-k
#         elif a[k]==0 and a[k+1]!=0 and a[k+2]==0:
#                 for m in range(a[k+1]):
#                     print(a[k],end=' ')
#                 k=k+3
#                 x=x-k
#         elif a[k]==0 and a[k+1]==0:
#                 print(a[k],end=' ')
#                 k=k+2
#                 x=x-k
#         else:
#             print(a[k],end=' ')
#             k=k+1
#             x=x-k
# except:
#     print(" ")