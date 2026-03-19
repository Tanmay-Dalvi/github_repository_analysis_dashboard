#!/usr/bin/env python
import sys

def main():
    current_language = None
    current_count = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
            
        try:
            language, count = line.split('\t', 1)
            count = int(count)
        except ValueError:
            continue

        if current_language == language:
            current_count += count
        else:
            if current_language:
                print("{}\t{}".format(current_language, current_count))
            current_language = language
            current_count = count

    # Output the last language
    if current_language:
        print("{}\t{}".format(current_language, current_count))

if __name__ == "__main__":
    main()
