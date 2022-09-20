n=int(input())
x=list(map(int,input().split()))
a=[]
c=0
for i in x:
    if i==x.count(i):
        if i not in a:
            a.append(i)
            c+=1
if c==0:
    print('-1')
else:
    print(*a)