from __future__ import print_function

import argparse
import os
import json
import sys


def parse_for_output(file_name):
    return('atlar')


def main(argv=None):
    return_code = 0
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to run on')
    args = parser.parse_args(argv)
    for filename in args.filenames:
        res = parse_for_output(filename)
        if res:
            print('{} output has been cleared'.format(filename))
            return_code = 1
    return return_code


if __name__ == '__main__':
    sys.exit(main())
