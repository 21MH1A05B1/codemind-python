n=int(input())
rev=0
if n>0:
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
        if n==0:
              print(rev)
else:
    n*=-1
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
        if n==0:
            rev=str(rev)
            print('-'+rev)