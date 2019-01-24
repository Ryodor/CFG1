import os

def bypass():
    """This method change the rights of every file to 777

    :return:
    """
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            os.chmod("../../Documents/" + name, 511)


def main():
    bypass()


if __name__ == '__main__':
    main()
