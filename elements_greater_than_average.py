n=int(input())
a=list(map(int,input().split()))
sum=0
c=0
for i in a:
    sum=sum+i
avg=(sum//n)
for i in a:
    if i>=avg:
        c+=1
print(c)

