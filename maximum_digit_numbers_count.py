def digit(n):
    if n==0:
        return 1
    c=0
    if n<0:
        n=-1*n
    while n:
        n//=10
        c+=1
    return c
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    b.append(digit(i))
for i in a:
    if digit(i)==max(b):
        print(i,end=' ')
   