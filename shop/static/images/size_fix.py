from PIL import Image
import os


def create_tubnails(name_img, size=(300,300)):
    try:
        img = Image.open(name_img)
        img.thumbnail(size)
        img.save(name_img)
    except Exception as e:
        print('create_tubnails error', e)


def make_square(name_img):
    try:
        img = Image.open(name_img)
        min_size = min(img.size)
        half_w = img.size[0] / 2
        half_h = img.size[1] / 2

        if img.size[0] == min_size:
            img5 = img.crop(
                (
                    half_w - half_w,
                    half_h - half_w,
                    half_w + half_w,
                    half_h + half_w
                )
            )
        elif img.size[1] == min_size:
            img5 = img.crop(
                (
                    half_w - half_h,
                    half_h - half_h,
                    half_w + half_h,
                    half_h + half_h
                )
            )

        img5.save(name_img)
    except Exception as e:
        print('make_square error', e)


def start():
    for _, _, files in os.walk('.', topdown=False):
        for pict in files:
            type_file = pict.split('.')[-1]
            if type_file == 'jpg':
                print(pict)
                make_square(pict)
                create_tubnails(pict)


start()
