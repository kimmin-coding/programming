import time

prev=time.time()
b=[i for i in range(100000)]

print(time.time()-prev)

a=[]
prev=time.time()
for i in range(100000):
    a.append(i)

print(time.time()-prev)


c=[]
prev=time.time()
for i in range(100000):
    c=c+[i]

print(time.time()-prev)