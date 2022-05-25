n=int(input())
a=list(map(int,input().split()))
sum=0
for i in a:
    for j in range(0,i+1):
        if i==j*j:
            sum+=i
print(sum)