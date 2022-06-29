n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
d=max(a)
f=0
for i in a:
    if d not in range(b,c+1):
        f=1
if f==1:
    print(d)
else:
    print('-1')