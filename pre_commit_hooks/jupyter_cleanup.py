from __future__ import print_function

import argparse
import os
import sys


def main(argv=None):
    return_code = 0
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to run on')
    args = parser.parse_args(argv)
    for filename in args.filenames:
        print(filename)
    try:
        assert 'common' in filename
    except:
        return 1
    return return_code


if __name__ == '__main__':
    sys.exit(main())
