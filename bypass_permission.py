import os

def bypass(path):
    """This method changes the rights of every file to 777

    :return:
    """
    os.chmod(path, 511)


def main():
    bypass("../../Documents/punpun.jpg")


if __name__ == '__main__':
    main()
