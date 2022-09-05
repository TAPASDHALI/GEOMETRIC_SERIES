## 2 - 6 + 18 - 54....N?
N = int(input("Enter N: "))
k = 2
sum = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        sum = sum - k
    else:
        sum = sum + k
    k = k * 3
print(f'Sum Of The Geometric Series: {sum}')
