#!/usr/bin/env python3
# https://en.wikipedia.org/wiki/Shebang_(Unix)

def count_vowels(input_str):
    """
    Function that counts up the number of vowels contained in the string s.
    Valid vowels are: 'a', 'e', 'i', 'o', and 'u'
    """
    count = 0
    in_str = input_str.lower()
    for s in in_str:
        if s in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count


# repr() function in python returns printable representation of object
# __name__ is stored in the global namespace

def main() -> object:
    word = 'Ambercrombie'
    print(count_vowels(word))


if __name__ == "__main__":
    main()
