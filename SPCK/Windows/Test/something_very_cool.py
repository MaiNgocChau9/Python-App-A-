# from datetime import datetime
# now = datetime.now()
# day = now.strftime("ngày %d tháng %m")
# time = int(now.strftime("%H"))

# print(f"Giờ: {time}")
# if time <= 11 and time >= 6:
#     print("Chào buổi sáng")
# elif time <= 13 and time >= 12:
#     print("Chào buổi trưa")
# elif time <= 6 and time >= 13:
#     print("Chào buổi chiều")
# else:
#     print("Chào buổi tối")
# print(f"Hôm nay là {day}")

import keyboard as kb

def on_key_event(e):
    if e.event_type == kb.KEY_DOWN and kb.is_pressed('ctrl+c'):
        print("Bạn vừa bấm tổ hợp phím Ctrl+C! 🎉")

# Đăng ký sự kiện
kb.hook(on_key_event)

# Giữ chương trình chạy
kb.wait('esc')  # Chờ đến khi bấm phím Esc để thoát
