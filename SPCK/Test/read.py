with open("SPCK\\data\\account.ecl", "r") as f:
    lines = f.readlines()
    logged = int(lines[1].split(":")[1])
print(logged)