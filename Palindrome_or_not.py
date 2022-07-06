def poli(n):
    if n.lower()==n.lower()[::-1]:
        return 1
n=input()
for i in n:
    if poli(n):
        print('True')
        break
    else:
        print('False')
        break
    