n=int(input())
a=list(map(int,input().split()))
e=[]
s=0
for i in a:
    if i not in e:
        e.append(i)
for i in e:
    if i%2==0:
        s=s+i
print(s)