def parent(num):
    def first_child():
        return "Hi, I am Zorawar"

    def second_child():
        return "Call me from J"

    if num == 1:
        return first_child
    else:
        return second_child


first = parent(1)
second = parent(2)

print(first())
print(second())
