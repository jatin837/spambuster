#!./env/bin/python

import argparse
import os

def get_args() -> tuple:
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="Path to input file")
    args = vars(ap.parse_args())

    ipath = os.path.abspath(args["input"])
    return (ipath)

def main() -> ():
    ipath = get_args()

    with open(ipath, 'r') as f:
        contents = f.readlines()

    print(contents)

if __name__ == "__main__":
    main()
