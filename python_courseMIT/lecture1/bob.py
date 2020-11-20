#!/usr/bin/env python3
"""
Write a program that prints the number of times the string 'bob'
occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""


def count_bob(in_str):
    in_str = in_str.lower()
    count = 0
    for i in range(len(in_str) - 2):
        if in_str[i:i + 3] == 'bob':
            count += 1
    return count


def main():
    word = 'bobbobobegghbob'
    print(count_bob(""))


if __name__ == "__main__":
    main()
