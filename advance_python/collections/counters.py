# Find top three letters in string
from collections import defaultdict
from collections import Counter
def top_three_letters(string):
    '''
    Given a string find the top three most frequent letters
    This method should return a list of tuples, where tuple contains
    the character and count
    '''
    # loop through the string and store the count for each letter
    # then sort dictionary by the count and find the top three most
    # frequent letters
    # return a formatted list to match the output
    # counter = defaultdict(int)
    # for c in string:
    #     counter[c] += 1
    # top_three = sorted(counter,
    #        key=lambda k:counter[k],
    #        reverse=True)[:3]
    #
    # return [(letter, counter[letter])
    #         for letter in top_three]
    print(Counter(string).most_common(3))


top_three_letters('abbbcc')