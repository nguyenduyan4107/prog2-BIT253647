class SinhVien:

    count = 0

    def __init__(self, name):
        self.name = name
        SinhVien.count += 1

    @classmethod
    def dem_sinh_vien(cls):
        return cls.count


sv1 = SinhVien("An")
sv2 = SinhVien("Hieu")
sv3 = SinhVien("Tam")

print(SinhVien.dem_sinh_vien())
