def prime(n):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                return False
        else:
            return True
    else:
         return False
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        if prime(i)==0:
            c+=1
print(c)