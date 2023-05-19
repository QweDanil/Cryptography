from PIL import Image, ImageDraw
from random import randint
from re import findall

class Picture():
    def stega_encrypt(self, pict, text):
        keys = []  # сюда будут помещены ключи
        img = Image.open(pict)  # создаём объект изображения
        draw = ImageDraw.Draw(img)  # объект рисования
        width = img.size[0]  # ширина
        height = img.size[1]  # высота
        pix = img.load()  # все пиксели тут
        f = open('keys.txt', 'w')  # текстовый файл для ключей

        for elem in ([ord(elem) for elem in text]):
            key = (randint(1, width - 10), randint(1, height - 10))
            g, b = pix[key][1:3]
            draw.point(key, (elem, g, b))
            keys.append(key)
            print(keys)
            f.write(str(key) + '\n')

        print('keys were written to the keys.txt file')
        img.save("newimage.png", "PNG")
        f.close()

    def stega_decrypt(self, pict):
        a = []
        keys = []
        img = Image.open(pict)
        pix = img.load()
        f = open("keys.txt", 'r')
        y = str([line.strip() for line in f])

        for i in range(len(findall(r'\((\d+)\,', y))):
            keys.append(
                (int(findall(r'\((\d+)\,', y)[i]), int(findall(r'\,\s(\d+)\)', y)[i])))
        for key in keys:
            a.append(pix[tuple(key)][0])
        return ''.join([chr(elem) for elem in a])



