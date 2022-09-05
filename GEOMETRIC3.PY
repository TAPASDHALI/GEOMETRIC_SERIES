## 10 + 30 + 90 + 270....N?
N = int(input("Enter N: "))
k = 10
sum = 0
for i in range(1, N + 1):
    sum = sum + k
    k = k * 3
print(f'Sum Of Geometric Series: {sum}')