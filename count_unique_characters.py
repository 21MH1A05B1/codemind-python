n=input()
n=n.lower()
n=n.replace(" ","")
l=list(n)
c=0
for i in l:
    if l.count(i)==1:
        c+=1
print(c)
        