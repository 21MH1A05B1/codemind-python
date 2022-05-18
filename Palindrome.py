n=int(input())
rev=0
while n:
    r=n%10
    rev=rev*10+r
    n=n//10
    if n==rev:
        print('True')
        break
else:
    print('False')
        