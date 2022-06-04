n=int(input())
a=n*n
temp=a
rev=0
rev2=0
while n:
    rem=n%10
    rev=rev*10+rem
    n=n//10
b=rev*rev
while b:
    rem=b%10
    rev2=rev2*10+rem
    b=b//10

if temp==rev2:
    print('True')
else:
    print('False')