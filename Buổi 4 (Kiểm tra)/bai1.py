class HinhVuong():
    def __init__(self, canh):
        self.canh = canh
    def tinh_chu_vi(self):
        return self.canh**2

hinhvuong = HinhVuong(float(input("Độ dài cạnh: ")))
print("Chu vi hình vuông:", hinhvuong.tinh_chu_vi())