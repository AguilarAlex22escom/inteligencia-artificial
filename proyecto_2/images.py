import os

def get_images(path):
    images = []
    images_name = os.listdir(path)
    for image in images_name:
        if image[-4:] == ".png":
            images.append(image)
    print(images)

get_images("shapes/dataset/")