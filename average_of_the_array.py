n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s+=i
avg=s/n
print('%.2f'%avg)
    