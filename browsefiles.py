import os
import pathlib


def browse_through_files(path):
    """ This method see through every file in the device and return each file
    in a list

    Args:
        Path(String): access path to browse the system

    Returns:  list_of_files ([]): A list filled with the name of each files

    """
    list_of_files = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if check_extension_file(os.path.join(root, name)) and find_size_file(os.path.join(root, name),1000000):
                list_of_files.append(os.path.join(root, name))
    return list_of_files


wh_extension = [".txt", ".png", ".pdf", ".jpeg", ".odp", ".zip", ".rar",".bmp"]


def check_extension_file(file):
    """ Check if the file is valid against the white list

    Args:
        file(file): file system

    Returns: valid file extension

    """

    for extension in wh_extension:
        if extension == pathlib.PurePosixPath(file).suffix:
            return True
    return False


def find_size_file(filename , max_size_file):
    """ Find size the file

    Args:
        filename(file): file

    Returns: Error message or retourn size file

    """

    if os.path.isfile(filename) and os.path.getsize(filename) <= max_size_file:
        return True
    return False


def main():
    return None


if __name__ == '__main__':
    main()


