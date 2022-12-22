n=input()
c=0
d=0
for i in n:
    if i in'aeiou':
        c+=1
    if i not in 'aeiou':
        if c>d:
            d=c
        c=0
if c>d:
    d=c
print(d)