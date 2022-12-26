a=input().split()
f='qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'
for i in a:
    c=[]
    for j in i:
        if j in f:
            c.append(j)
    c.sort()
    k=0
    for d in range(len(i)):
        if i[d] in f:
            print(c[k],end='')
            k+=1
        else:
            print(i[d],end='')
    print(end=' ')


    
        