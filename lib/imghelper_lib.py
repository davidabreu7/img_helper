import os
import sys


def parse_path(path):
    if os.path.isabs(path):
        if os.path.exists(path):
            if os.path.isfile(path):
                return [path]
            if os.path.isdir(path):
                return [os.path.abspath(file) for file in os.listdir(path) if os.path.isfile(file)]
        else:
            print("file not found")
            sys.exit(1)
    else:
        abs_path = os.path.join(os.getcwd(), path)
        if os.path.exists(abs_path):
            if os.path.isfile(abs_path):
                return [abs_path]
            if os.path.isdir(abs_path):
                return [os.path.abspath(file) for file in os.listdir(path) if os.path.isfile(file)]
        else:
            print("file not found")
            sys.exit(1)


def rotate_img(angle_arg, img_obj_list):
    angle = int(angle_arg[0])
    img_obj_list = [(img_obj.rotate(angle, expand=True), path) for img_obj, path in img_obj_list]
    return img_obj_list


def resize_img(sizes, img_obj_list):
    height, width = int(sizes[0]), int(sizes[1])
    new_size = (height, width)
    img_obj_list = [(img_obj.resize(new_size), path) for img_obj, path in img_obj_list]
    return img_obj_list


def change_format(new_format, img_obj_list):
    print(new_format)
