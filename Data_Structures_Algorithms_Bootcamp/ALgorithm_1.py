# Introduction, binary search and Big O notations
def binary_search(ip_list, item):
    low = 0
    high = len(ip_list) - 1

    while low <= high:
        mid = (low + high)//2
        guess = ip_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid - 1




