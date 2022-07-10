n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    i=str(i)
    le=len(i)
    b.append(le)
d=0
for i in b:
    if i==max(b):
        d+=1
print(d)
        