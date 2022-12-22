n=int(input())
for i in range(n):
    l=int(input())
    x=input() 
    c=0
    d=0
    for i in x:
        c=0
        for j in x:
            if i==j:
                c+=1
        if c==1:
            print(i)
            d+=1
            break
    if d==0:
        print('-1')