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
