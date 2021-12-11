import os
import sys


def parse_file(path_file: list[str]) -> dict:
    """
    read list of strings and returns dictionary of paths parsed_path[read:<file>, save:<file>
    if save dir does not exists, create it.
    :param path_file: list of strings of paths passed by CLI argument
    :return: dictionary with read and save paths
    """
    parsed_path = {}
    save_dir = os.path.dirname(path_file[1])

    if os.path.exists(path_file[0]) and os.path.isfile(path_file[0]):
        parsed_path["read"] = path_file[0]
    else:
        print("file not found")
        sys.exit(1)

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    parsed_path["save"] = path_file[1]

    return parsed_path


def parse_dir(path_dir: list[str]) -> dict:
    """
    read list of strings and returns dictionary of paths parsed_path[read:<file>, save:<file>
    if save dir does not exists, create it.
    :param path_dir: list of strings of paths passed by CLI argument
    :return: dictionary with read and save paths
    """
    parsed_path = {}
    if os.path.exists(path_dir[0]) and os.path.isdir(path_dir[0]):
        parsed_path["read"] = [os.path.join(path_dir[0], file) for file in os.listdir(path_dir[0])]

        if not os.path.exists(path_dir[1]):
            os.mkdir(path_dir[1])

        parsed_path["save"] = [os.path.join(path_dir[1], file) for file in os.listdir(path_dir[0])]
    else:
        print("folder not found")
        sys.exit(1)

    return parsed_path


def rotate_img(angle_arg, img_obj_list):
    """
    :param angle_arg:
    :param img_obj_list:
    :return: image object list
    """
    angle = int(angle_arg[0])
    img_obj_list = [img_obj.rotate(angle, expand=True) for img_obj in img_obj_list]
    return img_obj_list


def resize_img(sizes, img_obj_list):
    """
    :param sizes:
    :param img_obj_list:
    :return: image object list
    """
    height, width = int(sizes[0]), int(sizes[1])
    new_size = (height, width)
    img_obj_list = [img_obj.resize(new_size) for img_obj in img_obj_list]
    return img_obj_list

#
# def change_format(new_format, img_obj_list):
#     pass
#
#
# def add_prefix(prefix: list[str], img_ob_list):
#     pass
#
#
# def add_suffix(prefix: list[str], img_ob_list):
#     pass
