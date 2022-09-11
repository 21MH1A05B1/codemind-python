s=input().split(' ')
l=[]
for i in s:
    a=i[::-1]
    l.append(a)
print(*l)