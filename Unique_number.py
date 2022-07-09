n=int(input())
temp=n
le=len(str(n))
a=[]
c=0
while temp:
    rem=temp%10
    if rem not in a:
        a.append(rem)
        c+=1
    temp//=10
if c==le:
    print('Unique Number')
else:
    print('Not Unique Number')

    
    
    