def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
###0:0,1:1,2:1,3:2,4:3,5:5
n=int(input())#5
for i in range(n):
    print(fib(i),end=' ')#0

