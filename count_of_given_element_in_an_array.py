n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=0
for i in range(n):
    if a[i]==b:
        c+=1
if c==0:
    print('0')
else:
    print(c)