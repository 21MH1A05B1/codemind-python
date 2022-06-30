a=list(map(int,input().split(",")))
l=[]
for i in range(len(a)):
    s=0
    for j in range(1,(a[i]+1)):
        if a[i]%j==0:
            s+=j
    if s in a:
        l.append(a[i])
x=sorted(l)
for i in x:
    print(i,end=' ')
if len(l)==0:
    print("-1")
