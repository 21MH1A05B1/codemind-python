n=int(input())
a=list(map(int,input().split()))
max=a[0]
for i in range(n):
    if a[i]>max:
        max=a[i]
print(max)