x = open('17_7717.txt', 'r')
n=[int(i) for i in x.readlines()]
c = 0
mx = 0


def x(a):
    c = 0
    d = 0
    if len(str(a))%2==0:
        for i in str(a):
            if int(i)%2==0:
                c+=1
            else:
                d+=1
    if c == d:
        return True

def m(a,b):
    aa = 10
    bb = 0
    for i in str(a):
        if int(i) < aa:
            aa = int(i)
    for i in str(b):
        if int(i) > bb:
            bb = int(i)
    if aa > bb:
        return True

k=[]
for i in n:
    if x(i):
        k.append(i)
s = max(k)
print(s)


for i in range(len(n)-1):
    if m(n[i],n[i+1]):
        if n[i] + n[i+1] <s:
            c+=1
            if mx < n[i] + n[i+1]:
                mx = n[i] + n[i+1]
print(c,mx)