sa = int(input())
a = set(map(int,input().split()))
sb = int(input())
b = set(map(int,input().split()))

fs = sorted(list(a.difference(b))+list(b.difference(a)))
for n in fs:
    print(n)
