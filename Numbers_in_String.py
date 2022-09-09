n=input()
a='1234567890'
s=0
for i in n:
    if i in a:
        i=int(i)
        s+=i
print(s)