import os, argparse
from tabulate import tabulate

def long_format():
    return os.listdir()

def tabular_display(display_list):
    print(tabulate(display_list))

def main():
    parser=argparse.ArgumentParser(description="List file in directory from specified path")
    parser.add_argument('-l', action='store_true', help='Display in long format')
    args=parser.parse_args()
    if args.l:
        output=long_format()

    tabular_display(long_format())
    return long_format()


if __name__ == "__main__":
    main()