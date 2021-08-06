def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x*y

## Add logging to each function
# def add(x, y):
#     print('Calling add')
#     return x + y
#
# def sub(x, y):
#     print('Calling Sub')
#     return x - y
#
# def mul(x, y):
#     print('Calling mul')
#     return x*y

## How to resolve multiple print repeat
def logged(func):
    # Idea give me function I will put logging around it

    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)

    return wrapper

print(logged(add))
print(logged(sub))
print(logged(mul))

def textEditor1_2(queries):
    out_str = ""
    out_ls = []
    if len(queries) == 0:
        for text_list in queries:
            if text_list[0] == "APPEND":
                out_str += text_list[1]
            out_ls = out_ls.append(out_str)

    return out_ls