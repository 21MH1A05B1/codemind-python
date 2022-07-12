n=input()
n=n.lower()
n=n.split()
v='aeiou'
a=[]
c=0
for i in n:
    c=0
    for j in i:
        if j in v:
            c+=1
        a.append(c)
print(max(a))
