n=input()
n=n.lower()
n=n.split(' ')
c=0
for i in range(len(n)):
    a=''.join(n[i])
    if a[0] in 'aeiou' and a[len(a)-1] not in 'aeiou':
        c+=1
print(c)