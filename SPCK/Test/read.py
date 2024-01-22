with open("SPCK\\data\\account.ecl", "r") as f:
    lines = f.readlines()

    keep_me_login = int(lines[0].split(":")[1])
    logged = int(lines[1].split(":")[1])

print(keep_me_login)
print(logged)