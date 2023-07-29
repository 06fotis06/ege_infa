x = open('17_7718.txt', 'r')
n=[int(i) for i in x.readlines()]
c = 0
mx = 0
d =[]
for i in range(len(n)-1):
    for l in range(i+1,len(n)):
        if ((n[i]+n[l])%18==0 and (n[i]*n[l])%18 != 0) or ((n[i]+n[l])%18!=0 and (n[i]*n[l])%18 == 0) :
            c+=1
            if mx < (n[i]+n[l]):
                mx = (n[i]+n[l])

print(c,mx)