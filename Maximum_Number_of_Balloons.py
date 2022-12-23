n=input()
c1=n.count('b')
c2=n.count('a')
c3=n.count('l')
c4=n.count('o')
c5=n.count('n')
c3=c3//2
c4=c4//2
c=0
while c1!=0 and c2!=0 and c3!=0 and c4!=0 and c5!=0:
    c+=1
    c1-=1
    c2-=1
    c3-=1
    c4-=1
    c5-=1
print(c)
    