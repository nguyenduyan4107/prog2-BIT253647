import random

m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

matrix = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(1, 100))
    matrix.append(row)

print("Ma trận:")
for row in matrix:
    print(row)

r = int(input("Nhập hàng muốn xem: "))
print("Hàng", r, ":", matrix[r-1])

c = int(input("Nhập cột muốn xem: "))
print("Cột", c, ":")

for i in range(m):
    print(matrix[i][c-1])

max_value = matrix[0][0]

for row in matrix:
    for x in row:
        if x > max_value:
            max_value = x

print("Giá trị lớn nhất:", max_value)
