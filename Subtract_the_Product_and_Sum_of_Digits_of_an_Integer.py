n=int(input())
sum=0
mul=1
while n:
    r=n%10
    sum+=r
    mul*=r
    n=n//10
print(mul-sum)