def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
a=list(map(int,input().split()))
avg=0
c=0
for i in a:
    if i!=1:
        if prime(i):
                  avg=avg+i
                  c+=1
d=(avg/c)
print('%.2f'%d)