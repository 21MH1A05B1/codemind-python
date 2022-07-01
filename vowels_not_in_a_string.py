n=input()
n=n.lower()
s=''
s1='aeiou'
c=0
for i in n:
    if i in s1:
        s+=i
for i in s1:
    if i not in s:
        print(i,end=' ')
        c=1
if c!=1:
    print('0')