class HocSinh():
    def __init__(self, ten, diachi, chieucao, cannang, hocluc):
        self.HoVaTen = ten
        self.DiaChi = diachi
        self.ChieuCao = chieucao
        self.CanNang = cannang
        self.HocLuc = hocluc
    def Output(self):
        print("Họ và tên:", self.HoVaTen)
        print("Địa chỉ:", self.DiaChi)
        print("Chiều cao:", self.ChieuCao, "cm")
        print("Cân nặng:", self.CanNang, "kg")
        print("Học lực:", self.HocLuc)
        
#1. Khởi tạo để tạo đối tượng học sinh với tên, địa chỉ, chiều cao và cân nặng được cung cấp.
print("#1. Khởi tạo để tạo đối tượng học sinh với tên, địa chỉ, chiều cao và cân nặng được cung cấp.")
hocsinh = HocSinh("Mai Ngọc Châu", "Đồng Nai, Việt Nam", 158, 40, "Xuất sắc") #Cân nặng và Chiều cao có thể sai :vvv
hocsinh.Output()

# 2. Cập nhật địa chỉ mới khi học sinh chuyển nhà.
print("\n# 2. Cập nhật địa chỉ mới khi học sinh chuyển nhà.")
hocsinh.DiaChi = str(input("Nhập địa chỉ mới: "))

#3. Cập nhật chiều cao và cân nặng mới cho học sinh khi đến kỳ khám sức khỏe.
print("\n#3. Cập nhật chiều cao và cân nặng mới cho học sinh khi đến kỳ khám sức khỏe.")
hocsinh.ChieuCao = float(input("Nhập chiều cao: "))
hocsinh.CanNang = float(input("Nhập cân nặng: "))

#4. Xuất ra thông tin của học sinh
print("\n#4. Xuất ra thông tin của học sinh")
hocsinh.Output()