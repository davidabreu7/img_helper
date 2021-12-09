#!/home/dvlinux/PycharmProjects/img_helper/venv/bin/python3.10
from lib.imghelper_lib import *
from PIL import Image


def parse_arguments():
    import argparse
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
    add_argument('--path',
                 dest="path",
                 action='store',
                 nargs="+",
                 required=True,
                 )
    add_argument('--jpg',
                 dest="jpg",
                 action='store_true',
                 )
    add_argument('--prefix ',
                 dest='name',
                 action="store",
                 nargs="?",
                 )
    add_argument('--suffix ',
                 dest='name',
                 action="store",
                 nargs="?",
                 )
    return parser.parse_args()


def save_images(paths, image_obj_list):

    try:
        for index, file in enumerate(image_obj_list):
                file.save(paths.save[index])
                file.close()
        return True
    except OSError:
        print(f"Could not save file{OSError}")
        sys.exit(1)
    except ValueError:
        print(f"Could not save file: {ValueError}")
        sys.exit(1)


def main():
    args = parse_arguments()
    path = parse_path(args.path)

    try:
        image_obj_list = [Image.open(file) for file in path.read]
    except OSError:
        print(f"Could not read files in dir {os.path.dirname(path.read[0])}")
        sys.exit(1)

    if args.rotate:
        image_obj_list = rotate_img(args.rotate, image_obj_list)
    if args.size:
        image_obj_list = resize_img(args.size, image_obj_list)
    if args.jpg:
        image_obj_list = change_format(args.jpg, image_obj_list)

    if save_images(path, image_obj_list):
        print(f"Images saved in dir {os.path.dirname(path.save[0])}")
        sys.exit(0)


if __name__ == "__main__":
    main()
