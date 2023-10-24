import qrcode #import library yang akan dipakai
import image
qr = qrcode.QRCode(
    version = 15, #untuk versi qr codenya
    box_size = 10, #untuk ukuran qr codenya
    border = 5 #ukuran putih2nya qr code

)

data = "https://www.youtube.com/watch?v=a6sBJ0I93Ng" #link qr code

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color = "white") #setting warna qr code
img.save("link.png") #untuk build qr ke gambar png