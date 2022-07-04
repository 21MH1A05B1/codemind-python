def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=0
for i in a:
    if i!=1:
        if prime(i) and i>=b:
            c+=1
print(c)