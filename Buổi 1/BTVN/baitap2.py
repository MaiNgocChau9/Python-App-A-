def answer(result):
    result.sort()
    a = []
    for i in range(len(result)):
        if result[i]!=result[i-1]:
            a.append(result[i])
    return a
numbers = [1, 2, 2, 3, 4, 4, 5]
print("Danh sách sau khi loại bỏ phần tử trùng:", answer(numbers))


"""Cách 2
def loai_bo_trung(danh_sach):
    danh_sach_loai_bo_trung = []
    for phan_tu in danh_sach:
        if phan_tu not in danh_sach_loai_bo_trung:
            danh_sach_loai_bo_trung.append(phan_tu)
    return danh_sach_loai_bo_trung

danh_sach = [1, 2, 2, 3, 4, 4, 5]
print("Danh sách loại do các phân tử trùng nhau ", loai_bo_trung(danh_sach))
"""