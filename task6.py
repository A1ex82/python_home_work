import os
import logging
from collections import namedtuple

FileInfo = namedtuple('FileInfo', 'name ext is_dir parent_dir')

def gather_file_info(directory):
    logging.basicConfig(filename='file_info.log', level=logging.INFO)
    file_info_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            name, ext = os.path.splitext(file)
            file_info = FileInfo(name, ext[1:], False, os.path.basename(root))
            file_info_list.append(file_info)
            logging.info(f"File: {file_info}")
        for dir in dirs:
            file_info = FileInfo(dir, '', True, os.path.basename(root))
            file_info_list.append(file_info)
            logging.info(f"Dir: {file_info}")
    return file_info_list

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python file_info.py <directory>")
        sys.exit(1)
    directory = sys.argv[1]
    gather_file_info(directory)