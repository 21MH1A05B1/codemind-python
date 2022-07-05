n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s+=i
avg=s//n
for i in a:
    if i==avg:
        print('True')
        break
else:
    print('False')