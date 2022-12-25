n=int(input())
t=n
a=0
while t:
    a+=1
    t//=10
b=n
s=0
while n:
    s+=(n%10)**a
    n//=10
    a-=1
if s==b:
    print('True')
else:
    print('False')