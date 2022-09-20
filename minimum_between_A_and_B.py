n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
d=[]
c=0
for i in x:
    if i>=a and i<=b:
        d.append(i)
        c+=1
if c==0:
    print('-1')
else:
    print(min(*d))