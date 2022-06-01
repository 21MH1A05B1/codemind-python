def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
a=int(input())
b=int(input())
c=0
while a<=b:
    if prime(a):
        c+=1
    a+=1
print(c)