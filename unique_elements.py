n=int(input())
a=list(map(int,input().split()))
e=[]
for i in a:
    if i not in e:
        e.append(i)
print(*e)
    