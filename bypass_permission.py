import os

def bypass(path):
    """This method changes the rights of a file to 777

    Args:
        path (string): The path of the file you want to change chmod

    Return:
    """
    if os.access(path, os.R_OK) and os.access(path, os.W_OK) and os.access(path, os.X_OK):
        return False
    else:
        os.chmod(path, 511)
        return True


def main():
    print(bypass("../../Documents/punpun.jpg"))


if __name__ == '__main__':
    main()

