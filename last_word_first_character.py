n=list(map(str,input().split()))
c=0
for i in n:
    c+=1
    if c==len(n):
        print(i[:3:3])