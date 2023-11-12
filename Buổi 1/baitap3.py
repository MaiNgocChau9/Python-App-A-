a = str(input("Nhập một chuối: "))
b = ""
c = ""
for i in range(len(a)):
    if a[i] != " ":
        b += a[i]
a = b
b = list(b)
b.reverse()
for i in range(len(b)):
    c+=b[i]
if a==c:
    print("Đây là chuỗi đối xứng")
else:
    print("Đây không phải là chuỗi đối xứng")