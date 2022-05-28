n=int(input())
a=list(map(int,input().split()))
sum1=0
sum2=0
for i in range(len(a)):
    if a[i]%2==0:
        sum1=sum1+a[i]
    else:
        sum2=sum2+a[i]
if sum1>sum2:
    sum=sum1-sum2
else:
    sum=sum2-sum1
print(sum)
        