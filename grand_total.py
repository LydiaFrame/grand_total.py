#!/usr/bin/env python3

"""Program to read and total all numbers in a file."""

__author__ = 'Lydia Frame'
__date__ = '3/15/2025'

import sys

def main():
    """Read numbers from a file, handle exceptions, and calculate the total."""
    file_name = input('File? ')
    print()
    total = 0.0

    try:
        with open(file_name, 'r') as in_file:
            for line in in_file:
                line = line.strip()
                try:
                    total += float(line)
                except ValueError:
                    print('Invalid number:', line)
    except OSError:
        print('Could not open file - exiting')
        sys.exit()

    print('Grand total:', total)

if __name__ == '__main__':
    main()
