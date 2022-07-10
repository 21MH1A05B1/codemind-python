
def poli(n):
    rev=0
    temp=n
    while temp:
        r=temp%10
        rev=rev*10+r
        temp//=10
    if rev==n:
        return True
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if poli(i):
        c+=1
print(c)
  