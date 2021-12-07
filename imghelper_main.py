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
                 nargs=1,
                 default="images/"
                 )
    add_argument('-e',
                 dest="save",
                 action='store',
                 nargs=1,
                 )
    add_argument('-n',
                 dest='name',
                 action="store",
                 nargs=1,
                 )
    return parser.parse_args()


def main():
    args = parse_arguments()
    path = parse_path(args.path[0])
    image_obj_list = [(Image.open(file), path) for file in path]
    img_path = os.path.join(os.path.dirname(path[0]), "imghelper")

    if args.rotate:
        image_obj_list = rotate_img(args.rotate, image_obj_list)
    if args.size:
        image_obj_list = resize_img(args.size, image_obj_list)
    if args.save:
        image_obj_list = change_format(args.save, image_obj_list)

    if not os.path.exists(img_path):
        os.mkdir(img_path)

    for index, image in enumerate(image_obj_list):
        image_obj = image[0]
        image_path = image[1]
        print(image_path)
        image_obj.save(os.path.join(img_path, os.path.basename(image_path[index])))
        image_obj.close()


if __name__ == "__main__":
    main()
