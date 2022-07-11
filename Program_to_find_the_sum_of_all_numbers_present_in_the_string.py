n=input()
s=0
for i in n:
    if ord(i)>=49 and ord(i)<=57:
        s+=int(i)
print(s)