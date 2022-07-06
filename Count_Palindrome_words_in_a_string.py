def poli(s):
    if s.lower()==s.lower()[::-1]:
        return 1
def count_poli(s):
    c=0
    s=s.split(' ')
    for i in s:
        if poli(i):
            c+=1
    print(c)
n=input()
count_poli(n)