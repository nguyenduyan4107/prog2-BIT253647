# Bài 3
colors = ["Red", "Blue", "Green", "Yellow", "Black"]

try:
    colors.remove("Green")
except ValueError:
    print("Không tìm thấy Green")

print(colors)
