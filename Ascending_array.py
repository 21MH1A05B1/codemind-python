n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n-1):
    if a[i]<a[i+1]:
        c+=1
if c==(n-1):
    print('yes')
else:
    print('no')