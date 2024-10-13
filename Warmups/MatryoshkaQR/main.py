from PIL import Image
from pyzbar.pyzbar import decode
import io
import ast

data = decode(Image.open('qrcode.png'))
img_bytes = ast.literal_eval(f'b"{data[0].data.decode()}"')


flag = decode(Image.open(io.BytesIO(img_bytes)))
print(flag[0].data.decode())
