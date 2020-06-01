import Image

image = Image.open("pika.png")
width, height = image.size

binary_string = ""
for y in range(height):
    for x in range(width):
        #获取坐标(x, y)处的颜色值
        r, g, b = image.getpixel((x, y))
        color = (r << 16) + (g << 8) + b
        #获取颜色二进制值的最后一位
        last_bit = str(bin(color))[-1]
        binary_string += last_bit

print(binary_string)