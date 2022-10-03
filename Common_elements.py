a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
s=[]
s2=[]
l=[]
for i in x:
    if i not in s:
        s.append(i)
for j in set(y):
    if j not in s2:
        s2.append(j)
for i in s:
    for j in s2:
        if i==j:
            l.append(i)
print(*l)
            
