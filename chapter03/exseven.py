# Bài 7
arr = list(map(int, input("Nhập danh sách: ").split()))
x = int(input("Nhập số cần tìm: "))

found = -1

for i in range(len(arr)):
    if arr[i] == x:
        found = i
        break

if found != -1:
    print("Tìm thấy tại vị trí:", found)
else:
    print("Không tìm thấy")
