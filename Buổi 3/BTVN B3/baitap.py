class ThuCung():
    def __init__(self, ten, giong, mausac, tuoi, cannang):
        self.Ten = ten
        self.Giong = giong
        self.MauSac = mausac
        self.Tuoi = tuoi
        self.CanNang = cannang
    
    def xuatthongtin(self):
        print("Tên:", self.Ten)
        print("Giống:", self.Giong)
        print("Màu sắc:", self.MauSac)
        print("Tuổi:", self.Tuoi)
        print("Cân nặng:", self.CanNang)
    
    def doi_mau_long(self):
        self.MauSac = str(input("Đổi màu lông: "))

vatnuoi = ThuCung("Mèo", "Chó", "Đen", 2, 23)
vatnuoi.xuatthongtin()

print()
vatnuoi.doi_mau_long()
vatnuoi.xuatthongtin()
