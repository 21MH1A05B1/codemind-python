n=list(map(str,input().split()))
for i in range(len(n)):
    for j in range(len(n)):
        if i!=j and len(n[i])<len(n[j]):
            n[i],n[j]=n[j],n[i]
print(*n)