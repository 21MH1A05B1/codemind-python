n=int(input())
a=list(map(int,input().split()))
o=[]
for i in a:
    if i not in o:
        o.append(i)
c=0
for i in o:
    if i%2!=0:
        c+=1
print(c)
    