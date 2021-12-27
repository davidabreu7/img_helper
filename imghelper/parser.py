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
