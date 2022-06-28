n=int(input())
t=n
s=0
for i in range(1,(n//2)+1):
    if n%i==0:
        s+=i
if s==t:
    print('True')
else:
    print('False')