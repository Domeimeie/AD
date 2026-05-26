def hash(data):
    return sum(map(ord, data))

for item in ('hello world', 'world hello', 'gello xorld'):
    print("{}: {}".format(item, hash(item)))


