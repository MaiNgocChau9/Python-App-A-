from captcha.image import ImageCaptcha
image = ImageCaptcha(width=280, height=90)

import random
import string
captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
# Tạo một đối tượng ảnh với image.generate(captcha_text)
data = image.generate(captcha_text)

# Lưu ảnh vào một file với image.write()
image.write(captcha_text, 'captcha.png')
