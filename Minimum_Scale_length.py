n=int(input())
a=list(map(int,input().split()))
min=a[0]
for i in a:
    if i<min:
        min=i
while min>0:
    c=0
    for i in a:
        if i%min==0:
            c+=1
    if c==n:
        print(min)
        break
    else:
        min-=1
        