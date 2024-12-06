from random import random
from math import pi

n = int(input("Iteration number: "))

circle = 0
for i in range(n):
    x,y = random(),random()
    if x**2+y**2 <= 1:
        circle += 1

estimated = 4*circle/n
print(f"Estimated value of pi: {estimated}")
print(f"Error percentage: {abs(estimated-pi)*100/pi}")
