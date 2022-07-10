def ds(n):
    s=0
    while n:
        r=n%10
        s+=r
        n//=10
    return s
n=int(input())
a=list(map(int,input().split()))
s1=0
for i in a:
    s1+=ds(i)
print(s1)