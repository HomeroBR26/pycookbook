#! python3
from statistics import mean

# Use star to unpack multiple variables
def drop_first_last(grades):
    _, *middle, _ = grades
    print(middle)
    return mean(middle)


# Specially useful with tagged tuples
def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


def unpack_tagged(records):
    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)


# print(drop_first_last([1, 2, 3, 4, 5, 6, 7, 8]))
unpack_tagged([('foo', 1, 2), ('bar', 'ok'), ('foo', 3, 4)])

