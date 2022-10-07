n=input()
n1=input()
n=n.lower()
n1=n1.lower()
n=n.replace(" ","")
n1=n1.replace(" ","")
l=[]
for i in n:
    if i not in n1:
        l.append(i)
for j in n1:
    if j not in n:
        l.append(j)
for k in sorted(set(l)):
    print(k,end='')
