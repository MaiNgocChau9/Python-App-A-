class PhuongTien:
    def __init__(self, Loai_Xe, Hang_Xe, Mau_Sac, So_Cho_Ngoi, So_Banh_Xe, Gia_Tien):
        self.LoaiXe = Loai_Xe
        self.HangXe = Hang_Xe
        self.MauSac = Mau_Sac
        self.SoChoNgoi = So_Cho_Ngoi
        self.SoBanhXe = So_Banh_Xe
        self.GiaTien = Gia_Tien

    def XuatThongTin(self):
        print("Loại xe:", self.LoaiXe)
        print("Hãng xe:", self.HangXe)
        print("Màu sắc:", self.MauSac)
        print("Số chỗ ngồi:", self.SoChoNgoi)
        print("Số bánh xe:", self.SoBanhXe)
        print("Giá tiền:", self.GiaTien)

xe = PhuongTien()
xe.LoaiXe = "Model S Long Range"
xe.HangXe = "Tesla"
xe.MauSac = "Đen"
xe.SoChoNgoi = 4
xe.SoBanhXe = 4
xe.GiaTien = 18499000000
xe.XuatThongTin()