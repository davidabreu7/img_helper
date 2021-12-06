#!/home/dvlinux/PycharmProjects/img_helper/venv/bin/python3.10
from lib.imghelper_lib import *


def parse_arguments():
    import argparse
    parser = argparse.ArgumentParser()
    add_argument = parser.add_argument
    add_argument('-r',
                 dest="rotate",
                 action='store',
                 nargs=1,
                 )
    add_argument('-s',
                 dest="size",
                 action='store',
                 nargs=2,
                 )
    add_argument('--path',
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

    if args.rotate:
        rotate_img(args.rotate)
    elif args.size:
        resize_img(args.size)
    elif args.save:
        change_format(args.save)
    else:
        print("Opção inválida")


if __name__ == "__main__":
    main()
