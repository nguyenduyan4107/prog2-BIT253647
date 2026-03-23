r = int(input("Nhap so hang: "))
c = int(input("Nhap so cot: "))

A = []
B = []

for i in range(r):
    row = list(map(int, input().split()))
    if len(row) != c:
        print("Loi nhap")
        exit()
    A.append(row)

for i in range(r):
    row = list(map(int, input().split()))
    if len(row) != c:
        print("Loi nhap")
        exit()
    B.append(row)

C = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    C.append(row)

for row in C:
    print(row),
