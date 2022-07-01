n=input()
c=0
s=[]
for i in n:
    if i in 'AEIOUaeiou':
        if i not in s:
            s.append(i)
            c+=1
if c==0:
    print('-1')
else:
    print(*s)