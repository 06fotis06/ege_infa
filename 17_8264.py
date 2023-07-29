x = open('17_8264.txt', 'r')
n=[int(i) for i in x.readlines()]
f = min([abs(i) for i in n])
print(f)
c = 0
mx = 0
for i in range(len(n) - 1):
    if ((n[i] < 0 and n[i+1] >= 0) or  (n[i] >= 0 and n[i+1] < 0)) and (n[i] + n[i+1] > 0):
        if (n[i] + n[i + 1]) % f == 0:
            c+= 1
            if n[i] + n[i+1] > mx:
                mx = n[i] + n[i+1]


print(c, mx)