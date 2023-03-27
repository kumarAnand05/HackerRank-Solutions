if __name__ == '__main__':
    N = int(input())
    li = []
    for n in range(N):
        inp = input().split(' ')
        if len(inp) == 1:
            r = len(inp[0])
            if r == 3: li.pop()
            elif r == 4: li.sort()
            elif r == 5: print(li) 
            else: li = li[::-1]
        else:
            f = inp[0][0]
            if f == 'i': li.insert(int(inp[1]), int(inp[2]))
            elif f == 'r': li.remove(int(inp[1]))
            elif f == 'a': li.append(int(inp[1]))
            
