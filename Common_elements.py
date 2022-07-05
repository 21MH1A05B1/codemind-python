a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
e=[]
for i in x:
    if i in y and i not in e:
        e.append(i)
print(*e,end=' ')
    

    
        