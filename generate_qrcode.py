# QR Code Generate
#import  qrcode
#img = qrcode.make("https://www.youtube.com/channel/UCNphyzKdQKOu02VjLQ-N7Fg")
#type(img)
#img.save("youtbube.png")

# Advance QR Code
#import qrcode
#qr = qrcode.QRCode(
  #  version= 1,
  #  error_correction= qrcode.constants.ERROR_CORRECT_L,
   # box_size = 10,
   # border=4,
#)
#qr.add_data("https://www.youtube.com/channel/UCNphyzKdQKOu02VjLQ-N7Fg")
#qr.make(fit=True)
#img = qr.make_image(fill_color = "red", back_color = "green")
#img.save("Advance QR.png")

#
import qrcode
qr = qrcode.QRCode()
qr.add_data('https://www.linkedin.com/in/md-sharif-hossain-5724161aa/s')
img = qr.make_image()
img.save("Linkedin.png")
qr.clear()
qr.add_data('https://www.facebook.com/mdSharifHossaindu')
other_img = qr.make_image()
other_img.save("Facebook.png")
qr.add_data ('https://github.com/sharifdujee')
git_image = qr.make_image()
git_image.save('GitHub.png')
