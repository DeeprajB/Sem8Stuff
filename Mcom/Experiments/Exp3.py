# Find the orhtogonal between 2 vectors.
import numpy as np

n = int(input('\nNumber of data in a stream? '))
a = [0] * n
b = [0] * n
abak = [0] * n
bbak = [0] * n
c = [0] * n
for i in range(n):
    while True:
        try:
            a[i] = int(input("Enter the "+str(i)+"th value of a."), 2)
            b[i] = int(input("Enter the "+str(i)+"th value of b."), 2)
        except ValueError:
            print('Please make sure your number contains digits 0-1 only.')
        else:
            break

print("a="+str(a))
print("b="+str(b))

for i in range(n):
    if (a[i] == 0):
        a[i] = -1
    if (b[i] == 0):
        b[i] = -1

for i in range(n):
    bbak[i] = bbak[i]*-1

print("a="+str(a))
print("b="+str(bbak))

for i in range(n):
    c[i] = abak[i]+bbak[i]
print("c=", c)
print("The Value for Ak is", np.dot(c, a))
print("The Value for Bk is", np.dot(c, b))
