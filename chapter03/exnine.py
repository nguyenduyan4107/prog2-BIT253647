# Bài 9
arr = list(map(int, input("Nhập danh sách: ").split()))

for num in arr:
    if num % 2 != 0:
        print(num)
