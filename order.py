import os
import shutil
from enum import Enum, auto
from strenum import StrEnum
from typing import List

desktop_path = os.path.expanduser('~/Desktop')

extensions = ('.pdf', '.txt', '.py', '.docx', '.png')


def get_extension(p):
    return os.path.splitext(p)[1]


def fit_extension(p):
    ext = get_extension(p)
    if ext in extensions:
        return True
    return False


file_paths = list(filter(fit_extension, [os.path.join(desktop_path, x) for x in os.listdir(desktop_path)]))

print(file_paths)


class Criteria(Enum):
    DATE = auto()
    EXT = auto()


def order(files: List[str], criteria: Criteria):
    order_dir = os.path.join(desktop_path, 'order')
    if not os.path.isdir(order_dir):
        os.mkdir(order_dir)

    if criteria == Criteria.EXT:
        for ext in extensions:
            try:
                os.mkdir(os.path.join(order_dir, ext[1:].upper()))
            except:
                pass

        for f in file_paths:
            ext = get_extension(f)
            try:
                shutil.move(f, os.path.join(order_dir, ext[1:].upper()))
            except:
                pass
    else:
        pass


if __name__ == '__main__':
    order(file_paths, Criteria.EXT)
