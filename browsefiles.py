import os

def browse_through_files():
    """
    :return:
        list_of_files ([]): A list filled with the name of each files
    """
    list_of_files = []
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            list_of_files.append(name)
    return list_of_files


def main():
    list = browse_through_files()
    print(list)


if __name__ == '__main__':
    main()
