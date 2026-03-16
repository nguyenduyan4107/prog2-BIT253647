n = int(input("Nhap not so nguyen duong:  "))
original_n = n
tong = 0

while n > 0:
    chu_so = n%10
    tong += chu_so
    n = n //10
print(f"tong cac chu so cua {original_n} la: {tong}")
