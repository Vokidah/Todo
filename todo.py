__author__ = 'vokidah'

import sys


def ls():
    f = open('workfile', 'r')
    i = 1
    for line in f:
        print "%s. " % i + line,
        i += 1
    f.close()


def done():
    f = open('workfile', 'r')
    lines = f.readlines()
    f.close()
    f = open('workfile', 'w')
    for line in lines[1:]:
        f.write(line)
    f.close()


def add(data):
    f = open('workfile', 'a')
    print(data)
    f.write('\n%s' % data)
    f.close()


def next():
    f = open('workfile', 'r')
    data = f.readline()[:-1]
    f.close()
    print(data)


def main(argv):
    f = open('workfile', 'a')
    method_name = sys.argv[1]
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(method_name)
    if not method:
         raise NotImplementedError("Method %s not implemented" % method_name)
    if method_name == 'add':
        method(sys.argv[2])
    else:
        method()

if __name__ == "__main__":
   main(sys.argv[1:])

