from collections import OrderedDict, Counter

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


def allinstances(duplist):
    """Return a list with all items that occur more than once removed."""
    return [el for el, count in Counter(duplist).items() if count == 1]

if __name__ == '__main__':
    print(allinstances(duplist))
