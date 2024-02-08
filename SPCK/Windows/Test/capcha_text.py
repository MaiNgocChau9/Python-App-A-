from captcha.image import ImageCaptcha
import random
import string

# Kích thước hình ảnh mã captcha
image = ImageCaptcha(width=280, height=90)

# Tạo một chuỗi ngẫu nhiên cho CAPTCHA
captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Tạo một đối tượng ảnh với image.generate(captcha_text)
data = image.generate(captcha_text)

# Lưu ảnh vào một file với image.write()
image.write(captcha_text, 'captcha.png')