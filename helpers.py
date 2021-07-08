import argparse
import os

def get_args() -> tuple:
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="Path to input file")
    args = vars(ap.parse_args())

    ipath = os.path.abspath(args["input"])
    return (ipath)

def get_contents_from_file(path: str) -> str:
    with open(path, 'r') as f:
        contents = f.read()
    return contents

