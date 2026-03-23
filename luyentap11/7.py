import csv

name = input("Ten: ")
age = input("Tuoi: ")
id = input("ID: ")

with open("nhanvien.txt", "w", encoding="utf-8") as f:
    f.write(name + "," + age + "," + id)

with open("nhanvien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Ten", "Tuoi", "ID"])
    writer.writerow([name, age, id])

print("Da luu file")
