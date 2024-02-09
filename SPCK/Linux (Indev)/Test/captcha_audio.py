# Nhập module và tạo một đối tượng của AudioCaptcha
from captcha.audio import AudioCaptcha
audio = AudioCaptcha()

# Tạo một chuỗi số ngẫu nhiên cho CAPTCHA
import random
captcha_text = ''.join(random.choices('0123456789', k=6))

# Tạo một đối tượng âm thanh với audio.generate(captcha_text)
data = audio.generate(captcha_text)

# Lưu âm thanh vào một file với audio.write()
audio.write(captcha_text, 'captcha.wav')
