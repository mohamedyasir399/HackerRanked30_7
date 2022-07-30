import textwrap

def wrap(string, max_width):
    x =len(string)
    lst= []
    i =0
    while x >= i:
        lst.append(string[i:max_width+i])
        i += max_width
    return "\n".join(lst)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
