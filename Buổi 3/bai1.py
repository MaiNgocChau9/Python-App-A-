class PhuongTien:
    LoaiXe = "Tesla Model S Plaid"
    HangXe = "Tesla"
    MauSac = "Xám"
    SoChoNgoi = 4
    SoBanhXe = 4
    GiaTien = 22299000000

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