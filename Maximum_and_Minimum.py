n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    if i==a.count(i):
        if i not in b:
            b.append(i)
            c+=1
if c==0:
    print('-1')
else:
    print(min(b),max(b))
        