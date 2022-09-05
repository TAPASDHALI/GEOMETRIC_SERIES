## X*5^2/1+2! + X*25^2/2+3! + X*125^2/3+4!  ....N?
import math as m
N = int(input("Enter N: "))
X = int(input("Enter X: "))
k = 5
a1 = 1
a2 = 2
sum = 0
for i in range(1, N + 1):
    sum = sum + (X * k**2) / (a1+m.factorial(a2))
    k = k * 5
    a1 = a1 + 1
    a2 = a2 + 1
print(f'Sum Of The Geometric Series: {sum}')
