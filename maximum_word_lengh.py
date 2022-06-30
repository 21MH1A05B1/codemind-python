s=input()
s=s.split(' ')
n=[]
c=0
for i in range(len(s)):
    for j in s[i]:
        c+=1
    n.append(c)
    c=0
print(max(n))