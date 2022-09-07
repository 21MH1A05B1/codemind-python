def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
              return 0
    else:
        return 1
n1=int(input())
n2=int(input())
for i in range(1,10):
    if prime(n1+n2+i):
        print(i)
        break
