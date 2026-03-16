s = input("Nhap vao mot chuoi bat ky (khong dau): ")

in_hoa = 0
in_thuong = 0
chu_so = 0
khoang_trang = 0
ky_tu_dac_biet = 0
nguyen_am = 0
phu_am = 0

ds_nguyen_am = "aeiouAEIOU"

for char in s:

    if char.isalpha():

        if char.isupper():
            in_hoa += 1
        else:
            in_thuong += 1

        if char in ds_nguyen_am:
            nguyen_am += 1
        else:
            phu_am += 1

    elif char.isdigit():
        chu_so += 1

    elif char.isspace():
        khoang_trang += 1

    else:
        ky_tu_dac_biet += 1

print("-" * 30)
print(f"So luong chu cai in hoa:   {in_hoa}")
print(f"So luong chu cai in thuong: {in_thuong}")
print(f"So luong chu so:           {chu_so}")
print(f"So luong ky tu dac biet:   {ky_tu_dac_biet}")
print(f"So luong khoang trang:     {khoang_trang}")
print(f"So luong nguyen am:        {nguyen_am}")
print(f"So luong phu am:           {phu_am}")
