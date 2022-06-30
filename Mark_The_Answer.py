n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
t=0
for i in range(n):
    if a[i]<=k and t<2:
        c+=1
    else:
        t+=1
print(c)