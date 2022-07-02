import msvcrt

def input_between_strings (s, t):
    res = ''
    while True:
        print(s, res, t, sep = '', end = ' \r')
        curr = msvcrt.getch()[0]
        if curr == 13:
            print()
            return res
        elif curr == 8:
            res = res[:-1]
        else:
            res += chr(curr)