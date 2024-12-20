import qrcode

try:
    print("                            QR Code Generator")

    data = input("What Data you want to Store : ")
    nam = input("Name of QRCode : ")

    img = qrcode.make(data)
    
    img.save(f'{nam}.png')
except Exception as e:
    print(e)