n=input().lower()
n=n.split(' ')
for i in range(len(n)):
    a=list(n[i])
    for j in range(len(a)):
        for k in range(len(a)):
            if a[j]<a[k] and a[j] not in "aeiou" and a[k] not in "aeiou":
                a[j],a[k]=a[k],a[j]
    a=str(a)
    a=a.replace("[","")
    a=a.replace("]","")
    a=a.replace(" ","")
    a=a.replace(",","")
    a=a.replace("'","")
    print(a,end=' ')