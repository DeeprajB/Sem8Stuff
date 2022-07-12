# Find the orhtogonal between 2 vectors.
import numpy as np

n = int(input('\nNumber of data in a stream? '))
a = [0] * n
b = [0] * n
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


print("a="+str(a))
print("b="+str(b))

dotproduct = np.dot(a, b)
if(dotproduct == 0):
    print("Orthogonal")
else:
    print("Not Orthogonal")
