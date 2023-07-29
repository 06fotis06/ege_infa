x = open('17_7716.txt', 'r')
n=[int(i) for i in x.readlines()]
c = 0
mx = 0


def x(a):
    for i in str(a):
        if int(i) % 2 == 1:
            continue
        else:
            break
    return True

def m(a,b):
    aa = True
    bb = True
    for i in str(a):
        if int(i) % 2 == 0:
            continue
        else:
            aa = False
    for i in str(b):
        if int(i) % 2 == 0:
            continue
        else:
            bb = False
    if aa == True or bb == True:
        return True


k=[]
for i in n:
    if x(i):
        k.append(i)
s = max(k)
print(s)


for i in range(len(n)-1):
    if m(n[i],n[i+1]) and (n[i]+n[i+1])>s:
        c += 1
        if (n[i]+n[i+1]) > mx:
            mx = (n[i]+n[i+1])
print(c,mx)