a = 20
b = 18
c = 0
if max(a,b)%min(a,b)==0:
    c = max(a,b)/min(a,b)
else:
    for i in range(1, min(a,b)+1):
        if a%i == 0 and b%i == 0:
            c = i
print("Ước chung lớn nhất của", a, "và", b, "là:",c)