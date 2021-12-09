import os
import sys
from collections import namedtuple


def parse_path(paths: list[str]) -> namedtuple:
    # creating namedtuple with paths
    ImagePath = namedtuple("ImagePath", "read save")

    # parsing ImagePath.read
    ImagePath.read = os.path.abspath(paths[0])

    if os.path.exists(ImagePath.read):
        if os.path.isfile(ImagePath.read):
            ImagePath.read = [os.path.abspath(ImagePath.read)]
        if os.path.isdir(ImagePath.read[0]):
            dir_name = ImagePath.read
            list_dir = os.listdir(ImagePath.read)
            ImagePath.read = [os.path.join(dir_name, file) for file in list_dir if
                              os.path.isfile(os.path.join(dir_name, file))]
    else:
        print("file not found")
        sys.exit(1)

    # parsing ImagePath.save
    if len(paths) < 2:
        if os.path.isfile(paths[0]):
            ImagePath.save = [os.path.join(os.path.abspath(os.path.dirname(ImagePath.read[0])), "imghelper/",
                                           os.path.basename(paths[0]))]
        else:
            ImagePath.save = [os.path.join(os.path.abspath(paths[0]), "imghelper/")]

    else:
        ImagePath.save = [paths[1]]
        print(ImagePath.save)

    if not os.path.exists(ImagePath.save[0]):
        if os.path.sep == ImagePath.save[0][-1]:
            file_save_name = [os.path.basename(file) for file in ImagePath.read]
            dir_save_name = ImagePath.save[0]
            os.mkdir(ImagePath.save[0])
            ImagePath.save = [os.path.join(dir_save_name, file) for file in file_save_name]
    else:
        file_save_name = [os.path.basename(file) for file in ImagePath.read]
        dir_save_name = ImagePath.save[0]
        ImagePath.save = [os.path.join(dir_save_name, file) for file in file_save_name]
    return ImagePath


def rotate_img(angle_arg, img_obj_list):
    angle = int(angle_arg[0])
    img_obj_list = [img_obj.rotate(angle, expand=True) for img_obj in img_obj_list]
    return img_obj_list


def resize_img(sizes, img_obj_list):
    height, width = int(sizes[0]), int(sizes[1])
    new_size = (height, width)
    img_obj_list = [img_obj.resize(new_size) for img_obj in img_obj_list]
    return img_obj_list


def change_format(new_format, img_obj_list):
    pass


def add_prefix(prefix: list[str], img_ob_list):
    pass


def add_suffix(prefix: list[str], img_ob_list):
    pass
