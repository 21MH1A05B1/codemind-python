n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
d=max(x)
f=0
for i in x:
    if i not in range(a,b+1):
        f=1
if f==1:
    print(d)
else:
    print('-1')