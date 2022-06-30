n=int(input())
a=list(map(int,input().split()))
e=[]
for i in a:
    if i not in e:
        e.append(i)
c=0
for i in e:
    if i%2==0:
        c+=1
print(c)