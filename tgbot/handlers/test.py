# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from io import BytesIO,StringIO



img = Image.open('sertifikat.png')
I1 = ImageDraw.Draw(img)
myFont = ImageFont.truetype(font="shrift.ttf",size=110)
I1.text((540,500), "Turdiyev Alisher",font=myFont, fill =(22, 224, 224),align="center")
print(img)
# buf=BytesIO()
# img.save(buf,format='PNG')
# print(buf.flush())