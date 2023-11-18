from math import gcd

#input
tu = int(input("Nhập vào tử số: "))
mau = int(input("Nhập vào mẫu số: "))
ucln = gcd(tu, mau)

tu = int(tu/ucln)
mau = int(mau/ucln)

print(str(tu) + "/" + str(mau))