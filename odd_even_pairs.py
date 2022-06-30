n=int(input())
a=list(map(int,input().split()))
e=[]
o=[]
for i in range(0,n):
    if a[i]%2!=0:
        o.append(a[i])
    else:
        e.append(a[i])
i=0
j=0
while i<len(o) or j<len(e):
    if i<len(o):
        print(o[i],end=' ')
        i+=1
    if j<len(e):
        print(e[j],end=' ')
        j+=1
if n%2!=0:
    print('0')