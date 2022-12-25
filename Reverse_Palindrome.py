def rev(n):
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n//=10
    return rev
    
n=int(input())
while True:
    n+=rev(n)
    if n==rev(n):
        break
print(n)
    