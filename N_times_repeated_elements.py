n=int(input())
x=list(map(int,input().split()))
a=int(input())
d=[]
c=0
for i in x:
    if x.count(i)==a:
        if i not in d:
            d.append(i)
            c+=1
if c==0:
    print('-1')
else:
    print(*d)