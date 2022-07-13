n=input()
n=n.split()
s1=0
s2=0
for i in n:
    s1+=ord(min(i))
for i in n:
    s2+=ord(max(i))
print(abs(s2-s1))