from captcha.image import ImageCaptcha
image = ImageCaptcha(width = 280, height = 90)
captcha_text = 'isabele'
data = image.generate(captcha_text)
image.write(captcha_text, 'CAPTCHA.png')
