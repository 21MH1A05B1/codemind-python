s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s1=set(s1)
s2=set(s2)
c=0
for i in s1:
    if i!=' ':
        if i not in s2:
            c+=1
for i in s2:
    if i!=' ':
        if i not in s1:
            c+=1
print(c)
    