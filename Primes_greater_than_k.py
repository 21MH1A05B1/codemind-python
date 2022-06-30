def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=0
for i in a:
    if prime(i):
        if i>=b:
            c+=1
print(c)