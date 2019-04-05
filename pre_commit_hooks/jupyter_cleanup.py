from __future__ import print_function

import argparse
import json
import sys


def look_for_output_and_delete(file_name):
    updated = False
    with open(file_name) as json_file:
        try:
            content = json.load(json_file)
        except:
            return('not json compatible')
        # iterate over cells and clear output
        for a_cell in content['cells']:
            if a_cell.get('outputs'):
                updated = True
                a_cell['outputs'] = []
            if a_cell.get('execution_count'):
                updated = True
                a_cell['execution_count'] = None  # to be converted to null
    if updated:
        with open(file_name, 'w') as json_file:
            json.dump(content, json_file)
        return True
    else:
        return False


def main(argv=None):
    return_code = 0
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to run on')
    args = parser.parse_args(argv)
    for filename in args.filenames:
        res = look_for_output_and_delete(filename)
        if res == 'not json compatible':
            print('\nCAUTION')
            print('{} can not be opened as json'.format(filename))
        elif res:
            print('{} output has been cleared'.format(filename))
            return_code = 1
    return return_code


if __name__ == '__main__':
    sys.exit(main())
