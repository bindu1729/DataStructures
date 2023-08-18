#Valueerror
import os
import argparse
def check_for_empty_or_none(*args):
    for arg in args:
        if arg is None:
            raise Exception("One argument is None")
        if arg is None:
            raise Exception("One argument is empty")
def copy(source_file,target_file):
    """
    copy source file to target file
    :param source_file:
    :type source_file:String
    :param target_file:
    :return:
    :raises Exception when inputs or cannot copy a file
    """
    # if source_file is None or target_file is None:
    #     raise Exception("source or target file is None")
    # if source_file == "" or target_file == "":
    #     raise Exception("source or target file is empty string")
    check_for_empty_or_none(source_file,target_file)

    if not os.path.exists(source_file):
        raise Exception(f"{source_file} not found")

    with open(source_file, "r") as sfp:
        sfs_contents = sfp.read()
    with open(target_file, "w") as tfp:
        tfp.write(sfs_contents)

def move(source_file,target_file):
    check_for_empty_or_none(source_file,target_file)

    if not os.path.exists(source_file):
        raise Exception(f"{source_file} not found")

    with open(source_file, "r") as sfp:
        sfs_contents = sfp.read()
    with open(target_file, "w") as tfp:
        tfp.write(sfs_contents)
        os.remove(source_file)

if __name__ == '__main__':
    #source_file_path = "/Users/bindugutta/Desktop/Nanduri Algo/student.txt"
    #target_file_path = "/Users/bindugutta/Desktop/Nanduri Algo/student2.txt"
    parser = argparse.ArgumentParser(
        prog='Copy and Move file',
        description='this program copies or moves files.',
        epilog='file operations')
    parser.add_argument("action", choices=['copy', 'move'])
    parser.add_argument("--source-path", default='', help="Path to the source directory")
    parser.add_argument("--target-path", default='', help="Path to the target directory")

    args = parser.parse_args()
    if args.action == "copy":
        copy(source_file=args.source_path, target_file=args.target_path)
    elif args.action == "move":
        move(source_file=args.source_path, target_file=args.target_path)
    else:
        raise ValueError("invalid action chosen")
