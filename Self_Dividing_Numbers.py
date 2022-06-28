a=int(input())
b=int(input())
while a!=b+1:
    t=a
    c=0
    f=0
    while t%10!=0:
        d=t%10
        t=t//10
        if a%d==0:
            c+=1
        f+=1
    if c==f and a%10!=0:
          print(a,end=' ')
    a+=1