# Valueerror
# update rb and wb for binary files which includes text files aswell

# hw: md5 and sha in python and also verify before message
import os
import argparse


def check_for_empty_or_none(*args):
    for arg in args:
        if arg is None:
            raise Exception("One argument is None")
        if arg is None:
            raise Exception("One argument is empty")


def verify(source_file, target_file):
    with open(source_file, "rb") as sfp, open(target_file, "rb") as tfp:
        sfs_contents = sfp.read()
        tfp_contents = tfp.read()
    if sfs_contents == tfp_contents:
        return True
    else:
        return False


def copy(source_file, target_file):
    check_for_empty_or_none(source_file, target_file)

    if not os.path.exists(source_file):
        raise Exception(f"{source_file} not found")

    with open(source_file, "rb") as sfp, open(target_file, "wb") as tfp:
        for line in sfp.readlines():
            # print(line)
            tfp.write(line)
    if verify:
        print("Copied successfully")
    else:
        os.remove(target_file)
        print("not copied successfully")


def move(source_file, target_file):
    check_for_empty_or_none(source_file, target_file)

    if not os.path.exists(source_file):
        raise Exception(f"{source_file} not found")

    with open(source_file, "r") as sfp, open(target_file, "w") as tfp:
        for line in sfp.readlines():
            tfp.write(line)
    if verify:
        os.remove(source_file)
        if os.path.exists(source_file):
            print("copied but not moved")
        else:
            print("moved successfully")
    else:
        print("not moved successfully")


if __name__ == '__main__':
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
