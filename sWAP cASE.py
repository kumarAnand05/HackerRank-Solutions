def swap_case(s):
    r = ''
    for n in s:
        if (ord(n)) in range(65,91):r+=chr(ord(n)+32)
        elif(ord(n)) in range(97,123): r+=chr(ord(n)-32)
        else: r+=n
    return r

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
