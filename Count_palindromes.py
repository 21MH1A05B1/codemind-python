def poli(n):
    temp=n
    rev=0
    while temp:
        r=temp%10
        rev=(rev*10)+r
        temp//=10
    if rev==n:
        return True
    else:
        return False
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if poli(i)==True:
        c+=1
print(c)
    