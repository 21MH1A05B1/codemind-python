n=int(input())
a=list(map(int,input().split()))
m=a[0]
for i in a:
    if i<m:
        m=i
print(m)
