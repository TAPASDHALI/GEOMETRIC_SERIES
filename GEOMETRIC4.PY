## 5 + 25 + 125 + 625....N?
N = int(input("Enter N: "))
k = 5
sum = 0
for i in range(1, N + 1):
    sum = sum + k
    k = k * 5
print(f'Sum Of Geometric Series: {sum}')