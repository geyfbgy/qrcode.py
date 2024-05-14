import qrcode

qr = qrcode.make("https://youtu.be/3Y46v1ymdfQ?si=07kLlj4iiWaCxSpG")

qr.save("qr.jpg")
