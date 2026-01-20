import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask

# Shopee Brand Color (approximate Hex)
shopee_orange = (238, 77, 45) # #EE4D2D in RGB

# Create the QR Code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add the data
data = "https://mrnerdie12.github.io/1/"
qr.add_data(data)
qr.make(fit=True)

# Create the image with the specific color
img = qr.make_image(
    image_factory=StyledPilImage,
    color_mask=SolidFillColorMask(front_color=shopee_orange, back_color=(255, 255, 255))
)

# Save the image
filename = "shopee_surprise_qr.png"
img.save(filename)
