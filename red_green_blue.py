#!/usr/bin/env python3

# Created by Devin Jhu
# Created on May 2022
# RGB


def main():
    # this program shows the RGB
    red = 0
    green = 0
    blue = 0

    # process & output
    for red in range(255):
        for green in range(255):
            for blue in range(255):
                print("RGB {0}, {1}, {2}".format(red, green, blue))

    print("\nDone.")


if __name__ == "__main__":
    main()
