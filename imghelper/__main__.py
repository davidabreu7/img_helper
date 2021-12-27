import argparse
import os
import sys

from PIL import Image

from .imghelper_lib import rotate_img, resize_img
from .parser import parse_dir, parse_file


def parse_arguments():
    """
    Parse CLI arguments using argparse module
    :return: list of arguments strings
    """

    parser = argparse.ArgumentParser()
    add_argument = parser.add_argument
    add_argument('-r',
                 dest="rotate",
                 choices=["90", "180", "270"],
                 action='store',
                 nargs=1,
                 )
    add_argument('-s',
                 dest="size",
                 action='store',
                 nargs=2,
                 )
    add_argument('--file',
                 dest="file",
                 action='store',
                 nargs=2,
                 )
    add_argument('--dir',
                 dest="dir",
                 action='store',
                 nargs=2,
                 )
    # add_argument('--jpg',
    #              dest="jpg",
    #              action='store_true',
    #              )
    # add_argument('--prefix ',
    #              dest='name',
    #              action="store",
    #              nargs="?",
    #              )
    # add_argument('--suffix ',
    #              dest='name',
    #              action="store",
    #              nargs="?",
    #              )
    return parser.parse_args()


def save_path(image_obj_list, path_dir=None, path_file=None):
    """
    saves image object in read folder
    :param image_obj_list:
    :param path_dir:
    :param path_file:
    :return: True
    """
    try:
        if path_dir:
            for index, file in enumerate(image_obj_list):
                file.save(path_dir["save"][index])
                file.close()
            print(f"files saved in folder: {os.path.abspath(os.path.dirname(path_dir['save'][0]))}")
        if path_file:
            file = image_obj_list["save"]
            file.save(path_file)
            print(f"file saved in folder: {os.path.abspath(os.path.dirname(path_file['save']))}")

    except OSError:
        print(f"Could not save file{OSError}")
        sys.exit(1)
    except ValueError:
        print(f"Could not save file: {ValueError}")
        sys.exit(1)
    return True


def main():
    args = parse_arguments()
    path_file, path_dir = None, None
    image_obj_list = []
    try:
        if args.file:
            path_file = parse_file(args.file)
            image_obj_list = [Image.open(path_file["read"])]
        if args.dir:
            path_dir = parse_dir(args.dir)
            image_obj_list = [Image.open(file) for file in path_dir["read"]]

    except OSError:

        for arg in [args.file, args.dir]:
            if arg is not None:
                print(f"Could not read files in dir {os.path.dirname(arg['read'][0])}")
                sys.exit(1)

    if args.rotate:
        image_obj_list = rotate_img(args.rotate, image_obj_list)
    if args.size:
        image_obj_list = resize_img(args.size, image_obj_list)
    # if args.jpg:
    #     image_obj_list = change_format(args.jpg, image_obj_list)

    if save_path(image_obj_list, path_dir, path_file):
        sys.exit(0)


if __name__ == "__main__":
    main()
