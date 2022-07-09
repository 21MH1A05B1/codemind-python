n=int(input())
temp=n
a=temp*temp
rev=0
rev2=0
while temp>0:
    r1=temp%10
    rev=rev*10+r1
    temp=temp//10
b=rev*rev
while b>0:
    r=b%10
    rev2=rev2*10+r
    b//=10
if a==rev2:
    print('True')
else:
    print('False')