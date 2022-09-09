n=input().lower()
c1,c2,c3,c4=0,0,0,0
for i in n:
    if i in 'aeiou':
        c1+=1
    elif i.isdigit():
        c2+=1
    elif i==" ":
        c3+=1
    else:
        c4+=1
print("Vowels:",c1)
print("Consonants:",c4)
print("Digits:",c2)
print("White spaces:",c3)