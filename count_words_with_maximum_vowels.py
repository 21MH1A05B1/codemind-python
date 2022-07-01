s=list(map(str,input().split()))
c=0
a=[]
for i in s:
    for j in i:
        if j in "aeiou":
            c+=1
        elif j in 'AEIOU':
            c+=1
    a.append(c)
    c=0
print(a.count(max(a)))
        