x = open('17_7038.txt', 'r')
n=[int(i) for i in x.readlines()]
g = []
c = 0
for i in range(len(n) - 1):
    if  (str(n[i])[-1] == '1' and str(n[i+1])[-1] != '1') or (str(n[i])[-1] != '1' and str(n[i+1])[-1] == '1'):
        g.append([n[i],n[i+1]])
mxp = 0
for i in range(len(g) - 1):
    if (g[i][0] + g[i][1])/2 > mxp:
        mxp = (g[i][0] + g[i][1])/2

h = []
for i in range(len(g)):
    if g[i][0] < mxp and g[i][1] < mxp:
        c += 1
print(c)