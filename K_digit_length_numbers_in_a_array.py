a,b=map(int,input().split())
n=list(map(int,input().split()))
d=[]
for i in n:
    if i>=0:
        i=str(i)
        x=len(i)
        d.append(x)
    else:
        i=str(i)
        x=len(i)
        d.append(x-1)
c=0
for i in d:
    if i==b:
        c+=1
print(c)