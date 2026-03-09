import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c

if a <= b and a <= c:
    min_num = a
elif b <= a and b <= c:
    min_num = b
else:
    min_num = c

print("Số lớn nhất là:", max_num)
print("Số nhỏ nhất là:", min_num)


if a == 0:
    print("Không phải phương trình bậc 2")
else:
    delta = b*b - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)

        print("Phương trình có 2 nghiệm:")
        print("x1 =", x1)
        print("x2 =", x2)

    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép:", x)

    else:
        print("Phương trình vô nghiệm")
