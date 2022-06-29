a,b=map(int,input().split())
if a%2==0 and (b%2==0 or a>0):
    print('YES')
else:
    print('NO')