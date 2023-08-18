
import argparse
def copy(source_file,target_file):
    with open(source_file, "r") as sfp:
        sfs_contents = sfp.read()
    with open(target_file, "w") as tfp:
        tfp.write(sfs_contents)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["copy"], help="Action to perform: copy")
    parser.add_argument("--source-path", help="Path to the source directory")
    parser.add_argument("--target-path", help="Path to the target directory")

    args = parser.parse_args()

    source_path = args.sourcepath
    target_path = args.path
    copy(source_file=source_path,target_file=target_path)