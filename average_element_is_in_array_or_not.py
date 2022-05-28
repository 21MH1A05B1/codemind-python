n=int(input())
a=list(map(int,input().split()))
su=0
for i in range(n):
    su=su+a[i]
avg=su//n
    
if avg in a:
    print('True')
else:
    print('False')
