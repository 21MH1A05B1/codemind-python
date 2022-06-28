def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
c=0
for i in range(2,(n//2)+1):
    if n%i==0:
        if prime(i) and prime(n//i):
            print(i,n//i)
            c=1
            break
if c!=1:
    print('-1')