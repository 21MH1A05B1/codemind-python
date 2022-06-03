n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    if i%2!=0 and a[i]%2==0:
        c+=1
if c==0:
    print('True')
else:
    print('False')