# Bài 8
arr = list(map(int, input("Nhập danh sách: ").split()))

for num in arr:
    if num > 10:
        print("Số đầu tiên > 10 là:", num)
        break
else:
    print("Không có số nào > 10")
