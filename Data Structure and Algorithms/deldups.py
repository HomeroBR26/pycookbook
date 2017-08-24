from collections import OrderedDict

duplist = "@#$@o#$#@$@#$#$@#k@#$@#$i@#$@#$@#$@#$@"


def unordered(duplist):
    """Return a list with all unordered different elements in iterable duplist."""
    return list(set(duplist))


def ordered(duplist):
    """Return a list deleting duplicates and keeping order of original iterable."""
    s = []

    for elem in list(OrderedDict.fromkeys(duplist)):
        if duplist.count(elem) == 1:
            s.append(elem)

    return s

if __name__ == '__main__':
    print(unordered(duplist))
