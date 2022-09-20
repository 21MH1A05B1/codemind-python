n=int(input())
x=list(map(int,input().split()))
a=int(input())
d=[]
c=0
for i in x:
    if x.count(i)==a:
        d.append(i)
e=set(d)
if len(e)==0:
    print('-1')
else:
    print(*e)
        