import qrcode


url = "https://github.com/Imron0250/Andijon-Footboll"

img = qrcode.make(url)
img.save("p2d.png")
print("[+] QR code done")