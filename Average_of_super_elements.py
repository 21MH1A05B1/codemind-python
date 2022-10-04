n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in set(a):
    if i==a.count(i):
        s+=i
        c+=1
if c==0:
    print('-1')
else:
    avg=s/c
print('%.2f'%avg)