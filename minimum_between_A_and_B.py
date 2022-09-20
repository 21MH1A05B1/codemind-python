n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
c1=0
for i in x:
    if i>=a and i<=b:
        c.append(i)
        c1=1
if (c1==0):
    print('-1')
else:
    print(min(c))