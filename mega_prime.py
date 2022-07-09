def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
temp=n
c=d=0
while n:
    rem=n%10
    c+=1
    n//=10
    if prime(rem):
        d+=1
if c==d and prime(temp):
    print('Mega Prime')
else:
    print('Not Mega Prime')
    
