n=input()
n=n.lower()
n=n.replace(" ","")
c=0
for i in n:
    if n.count(i)==1:
        print(i)
        c+=1
        break
if c==0:
    print('-1')
    