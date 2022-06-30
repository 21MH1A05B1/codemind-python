n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
x=0
for i in range(n):
    if a[i]>=b and a[i]<=c:
        print(a[i],end=' ')
        x+=1
if x==0:
    print('-1')
