import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://otakukart.com/wp-content/uploads/2021/01/Jujutsu-Kaisen-Itadori-Yuji.jpg")
# print(r.status_code)
img = Image.open(BytesIO(r.content))
print(img.size, img.mode , img.format)
path = "./img/itadori." + img.format

try:
    img.save(path, img.format)
except IOError:
    print("cannot fetch")


