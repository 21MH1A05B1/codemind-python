def dig(n):
    s=0
    while n:
        s+=n%10
        n//=10
    return s
n=int(input())
a=list(map(int,input().split()))
s2=0
for i in a:
    s2+=dig(i)
print(s2)