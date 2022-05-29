n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    if a[i]%2==0:
        x=a[i]
print(x)