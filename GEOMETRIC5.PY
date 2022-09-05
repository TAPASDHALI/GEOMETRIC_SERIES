## X/2 + X/4 + X/8 + X/16....N?
N = int(input("Enter N: "))
X = int(input("Enter X: "))
k = 2
sum = 0
for i in range(1, N + 1):
    sum = sum + X/k
    k = k * 2
print(f'Sum Of Geometric Series: {sum}')