n=int(input())
a=list(map(int,input().split()))
s=c=0
for i in set(a):
    if a.count(i)==i:
        s+=i
        c+=1
if c==0:
    print('-1')
else:
    b=s/c
print("%.2f"%b)