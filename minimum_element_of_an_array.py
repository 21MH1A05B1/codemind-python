n=int(input())
a=list(map(int,input().split()))
min=a[0]
for i in a:
    if i<min:
        min=i
print(min)