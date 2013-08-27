#!/usr/bin/python

import re
import sys

dimen = '<dimen name=\"(.*?)\">(\d+)(.*?)</dimen>'
dimen_format = '<dimen name=\"{0}\">{1}{2}</dimen>\n'


def main(args):
    if len(args) != 3:
        print 'Usage: python multiple.py <multiplying_power> <input_file_path> <output_file_path>'
        sys.exit(1)

    with open(args[1]) as fin, open(args[2], 'w') as out:
        for line in fin:
            match = re.search(dimen, line)
            if match:
                value = int(match.group(2)) * float(args[0])
                text = dimen_format.format(match.group(1),
                                           value,
                                           match.group(3))
                out.write(text)
            else:
                out.write(line)

if __name__ == '__main__':
    main(sys.argv[1:])
