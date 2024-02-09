from datetime import datetime
now = datetime.now()
day = now.strftime("ngày %d tháng %m")
time = int(now.strftime("%H"))

print(f"Giờ: {time}")
if time <= 13 and time >= 6:
    print("Chào buổi sáng")
elif time <= 6 and time >= 13:
    print("Chào buổi chiều")
else:
    print("Chào buổi tối")
print(f"Hôm nay là {day}")