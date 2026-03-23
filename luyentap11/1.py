arr = []

for i in range(5):
    s = input(f"Nhap chuoi {i+1}: ")
    arr.append(s)

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and len(arr[j]) < len(key):
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

    print("Buoc", i, ":", arr)

print("Ket qua:", arr)
