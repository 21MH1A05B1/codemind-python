n=int(input())
a=list(map(int,input().split()))
b=int(input())
ind=-1
for i in range(0,n):
    if a[i]==b:
        ind=i
        break
print(ind)