import os

def bypass(path):
    """This method changes the rights of a file to 777

    Args:
        path (string): The path of the file you want to change chmod

    :return:
    """
    os.chmod(path, 511)


def main():
    bypass("../../Documents/punpun.jpg")


if __name__ == '__main__':
    main()
