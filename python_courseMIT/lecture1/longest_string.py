#!/usr/bin/env python3
"""
Write a program that prints the longest substring of s in which
the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc
"""


def long_substring(in_str):
    in_str = in_str.lower()
    count = 0
    max_count = 0
    result = 0
    for i in range(len(in_str)-1):
        if in_str[i] <= in_str[i+1]:
            count += 1
            if count > max_count:
                max_count = count
                result = i + 1
        else:
            count = 0
    start_position = result - max_count
    return in_str[start_position:result+1]


def main():
    in_str = 'abcdefghasdwf'
    long_string = long_substring(in_str)
    print(long_string)


if __name__ == "__main__":
    main()
