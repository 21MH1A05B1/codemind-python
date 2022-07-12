n=input()
n=n.lower()
n=n.replace(" ","")
r=[]
c=0
for i in n:
    if n.count(i)==1:
        r.append(i)
        c+=1
print(c)

        
        