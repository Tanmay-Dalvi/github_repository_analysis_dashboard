#!/usr/bin/env python
import sys
import csv

def main():
    # Use csv module to handle quoted fields correctly
    reader = csv.DictReader(sys.stdin)
    for row in reader:
        language = row.get('language', '').strip()
        if language:
            # Emit language and count 1
            print("{}\t1".format(language))

if __name__ == "__main__":
    main()
