# Bài 10
arr = list(map(int, input("Nhập danh sách: ").split()))

total = 0

for num in arr:
    if num % 2 == 0:
        print(num)
        total += num

print("Tổng số chẵn:", total)
