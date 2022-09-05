## 2 + 4 + 8 + 16.....N
from msvcrt import kbhit


N = int(input("Enter N: "))
sum = 0
k = 2
for i in range(1, N + 1):
    sum = sum + k
    k = k * 2
print(f'Sum Of Geometric Series: {sum}')