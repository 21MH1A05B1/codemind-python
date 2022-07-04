n=int(input())
a=list(map(int,input().split()))
o=[]
s=0
for i in a:
    if i not in o:
        o.append(i)
for i in o:
    if i%2!=0:
        s=s+i
print(s)