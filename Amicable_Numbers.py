a=int(input())
b=int(input())
s=0
for i in range(1,(a//2)+1):
    if a%i==0:
        s+=i
    i+=1
if s==b:
    s=0
    for i in range(1,(b//2)+1):
        if b%i==0:
            s+=i
        i+=1
if s==a:
    print('Amicable')
else:
    print('Not Amicable')