n=int(input())
a=list(map(int,input().split()))
for i in a:
    if i>=0:
        i=str(i)
        l=len(i)
        print(l,end=' ')
    else:
        i=str(i)
        l=len(i)
        print(l-1,end=' ')
    
