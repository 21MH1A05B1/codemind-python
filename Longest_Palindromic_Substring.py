def strrev(s):
    if len(s)==1:
        return s
    t=""
    for i in range(len(s)-1,-1,-1):
        t+=s[i]
    return t
    
s=input()
s1=''
m=0
for i in range(len(s)):
    s2=""
    for j in range(i,len(s)):
        s2+=s[j]
        if s2==strrev(s2):
            if s2 in s and len(s2)>m:
                s1=s2
                m=len(s1)
print(s1)