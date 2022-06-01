n=int(input())
for i in range(0,n):
    a=int(input())
    res=1
    for i in range(1,a+1):
        res*=i
    print(res)