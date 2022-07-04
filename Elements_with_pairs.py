n=int(input())
a=list(map(int,input().split()))
for i in a:
    print(i,end=' ')
if n%2!=0:
    print('0',end=' ')