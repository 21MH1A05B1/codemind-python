def digit(n):
    if n==0:
        return True
    c=0
    while n!=0:
        n//=10
        c+=1
    return c
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    b.append(digit(i))
c=max(b)
print(b.count(c))