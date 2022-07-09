n=int(input())
temp=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
a=abs(rev)
if temp==a:
    print('True')
else:
    print('False')