n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
sum=0
for i in a:
    if i<b or i>c:
        sum=sum+i
print(sum)
        