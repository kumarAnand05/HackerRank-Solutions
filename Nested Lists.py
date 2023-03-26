if __name__ == '__main__':
    records = []
    s = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        s.append(score)
        records.append([name,score])
    
    res = sorted([x[0] for x in records if x[1] == sorted(set(s))[1]])
    for n in res:
        print(n)
