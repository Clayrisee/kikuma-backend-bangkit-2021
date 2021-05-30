from model.model import Model
import os
import base64
# from tensorflow.keras.preprocessing import image
import io
from PIL import Image

IMG_PATH = os.path.join(os.getcwd(),'test_images','acne-cystic-11.jpg')
encoded_img =''
with open(IMG_PATH, "rb") as image2string:
    encoded_img = base64.b64encode(image2string.read())
print(encoded_img)
print(type(encoded_img))

# base64_decode = base64.b64decode(encoded_img)

# print(type(base64_decode))
# # img = image.load_img(io.BytesIO(base64_decode))
# img = Image.open(io.BytesIO(base64_decode))
# print(type(img))
# print(img.size)
# img_resize = img.resize((224, 224), Image.ANTIALIAS)
# print(img_resize.size)
# img_resize.show()
# # im
model = Model()

prediction= model.predict(encoded_img)
print(prediction)