a=list(map(int,input().split()))
b=max(a)
for i in range(0,len(a)):
    if a[i]==b:
        a[i]=0
        break
c=max(a)
m=(b-1)*(c-1)
print(m)