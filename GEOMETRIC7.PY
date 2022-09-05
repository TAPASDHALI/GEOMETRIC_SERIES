## X+2/10 + X+4/30 + X+6/90 + X+8/270....N?
N = int(input("Enter N: "))
X = int(input("Enter X: "))
a = 2
k = 10
sum = 0
for i in range(1, N + 1):
    sum = sum + (X + a) / k
    a = a + 2
    k = k * 3
print(f'Sum Of The Geometric Series: {sum}')
