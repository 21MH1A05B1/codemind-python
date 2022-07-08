
n=int(input())
t=n
rev=0
c=0
ans=0
while t:
    r=t%10
    rev=rev*10+r
    t=t//10
while rev:
    r=rev%10
    if r==6 and c==0:
        r=9
        c+=1
    ans=(ans*10)+r
    rev=rev//10
print(ans)
