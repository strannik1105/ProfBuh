from PIL import Image
from imgcompare import image_diff_percent


def compare(img_1, img_2):
    image_1 = Image.open(img_1.path)
    image_2 = Image.open(img_2.path)
    img_1_resized = image_1.resize((400, 300))
    img_2_resized = image_2.resize((400, 300))
    percent = image_diff_percent(img_1_resized, img_2_resized)
    return percent
