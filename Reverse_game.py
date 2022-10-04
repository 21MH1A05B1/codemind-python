def poli(n):
    temp=n
    rev=0
    while temp:
        r=temp%10
        rev=(rev*10)+r
        temp//=10
    return rev
n=int(input())
a=list(map(int,input().split()))
for i in a:
    print(poli(i),end=' ')
        
        
