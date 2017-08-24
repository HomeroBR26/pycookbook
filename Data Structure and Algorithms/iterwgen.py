

def frange(start, stop, increment=0.1):
    x = start
    while x < stop:
        yield x
        x += increment

if __name__ == '__main__':
    for f in frange(0, 1):
        print(f)

    for f in frange(0, 1):
        print(f)
