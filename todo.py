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
    if sys.argv[2:]:
        if method_name == 'add':
            params = sys.argv[2]
            add(params)
        else:
            print("Function doesn't take any parameters , please try again")
    else:
        if method_name == 'done':
            done()
        elif method_name == 'next':
            next()
        elif method_name == 'ls':
            ls()
        else:
            print("No function found")
if __name__ == "__main__":
   main(sys.argv[1:])

