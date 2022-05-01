import os

DIRECTORY = r"A:\Проекты\Разработки\Python\FindContentFiles\Test"


def find(find_directory):
    for root, dirs, files in os.walk(find_directory):
        for name in files:
            find_text_in_file(os.path.join(root, name))


def find_text_in_file(file):
    f = open(file, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    write_text_to_file(text)


def write_text_to_file(text):
    f = open("4.txt", 'a', encoding='utf-8')
    f.write(text)
    f.close()


if __name__ == '__main__':
    find(DIRECTORY)
