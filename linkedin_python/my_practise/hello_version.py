#!/usr/bin/env python3

import platform


def message():
    print('This is python version {}'.format(platform.python_version()))
    print(f'This is python version {platform.python_version()}')  # f string
    x = 42
    print('Hello, World. {}'.format(x))


def main():
    message()


if __name__ == "__main__":
    main()
