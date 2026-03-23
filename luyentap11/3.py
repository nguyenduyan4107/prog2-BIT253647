nums = list(map(int, input("Nhap danh sach so: ").split()))

even_nums = []
tong = 0

for n in nums:
    if n % 2 == 0:
        even_nums.append(n)
        tong += n

print("So chan:", even_nums)
print("Tong:", tong)
