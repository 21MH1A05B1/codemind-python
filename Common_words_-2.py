s1=input()
s2=input()
s1=s1.split()
s2=s2.split()
a=[]
b=[]
c=0
for i in s1:
    if s1.count(i)==1:
        a.append(i)
for i in s2:
    if s2.count(i)==1:
        b.append(i)
for i in a:
    if i in b:
        c+=1
print(c)
        