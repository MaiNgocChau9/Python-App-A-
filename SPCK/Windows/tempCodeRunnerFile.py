        captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        image.write(captcha_text, 'captcha.png')