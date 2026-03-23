d = {}

n = int(input("Nhập số người: "))

for i in range(n):
    name = input("Tên: ")
    age = int(input("Tuổi: "))
    d[name] = age

tong = sum(d.values())
avg = tong / len(d)

print("Tuổi trung bình:", avg)
