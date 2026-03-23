import math

lst = list(map(int, input("Nhap danh sach: ").split()))

x = int(input("Them phan tu: "))
lst.append(x)

k = int(input("Nhap k: "))
print("So lan xuat hien:", lst.count(k))

tong = 0

for n in lst:
    if n > 1:
        prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                prime = False
                break
        if prime:
            tong += n

print("Tong so nguyen to:", tong)

lst.sort()
print("Sap xep:", lst)

lst.clear()
print("Danh sach sau khi xoa:", lst)
