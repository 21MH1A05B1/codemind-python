s=input()
s=s.split(' ')
c=0
for i in range(len(s)):
    for j in s[i]:
        c+=1
    print(c,end=' ')
    c=0