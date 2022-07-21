a=[0,6,4,0,0,71,71,0,4,5]
k=0
for i in range(k,len(a)):
    if a[i]==0 and a[i+1]!=0 and a[i+2]!=0:
        k=i+(i+3)
        for j in range(a[i+1]):
            print(a[i+2],end=' ')
    if a[i]==0 and a[i+1]==0:
        k=i+(i+2)
        print(a[i],end=' ')
    k=i+10