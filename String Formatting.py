'''
#it's not accpeted answer yet!!
def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):  
        print('{:>2d} {:>2o} {:>2X} {:>2b}'.format(i,i,i,i))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    '''


def binary(i):
    r = ''
    while i != 0:
        if i % 2 == 0:
            r += '0'
        else:
            r += '1'
        i //= 2
    return r[::-1]


def octal(i):
    r = ''
    while i != 0:
        r += str(i % 8)
        i //= 8
    return r[::-1]


def hexa(i):
    r = ''
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while i != 0:
        if i % 16 in dic.keys():
            r += dic[i % 16]
        else:
            r += str(i % 16)
        i //= 16
    return r[::-1]


def print_formatted(number):
    # your code goes here
    for i in range(1, number + 1):
        o = octal(i)
        h = hexa(i)
        b = binary(i)
        print("{:6d} {:6s} {:6s} {:6s}".format(i, o, h, b))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
