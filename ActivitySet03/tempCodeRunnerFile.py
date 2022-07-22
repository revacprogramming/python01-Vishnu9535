# a=[1,0,2,0,0,10,1,2,3,4,0,3,0,2]
# k=0
# x=len(a)

# try:
#     for i in range(k,x):
#         if a[k]==0 and a[k+1]!=0:
#             for j in range(a[k+1]):
#                 print(a[k+2],end=' ')
#             k=k+3
#             x=x-k
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