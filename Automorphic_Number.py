n=int(input())
sq=n*n
t=n
rev=0
d=0
while t:
    d+=1
    t=t//10
while d:
    r=sq%10
    rev=rev*10+r
    sq=sq//10
    d-=1
rev1=0
while rev:
    r=rev%10
    rev1=rev1*10+r
    rev=rev//10
if rev1==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
    
    