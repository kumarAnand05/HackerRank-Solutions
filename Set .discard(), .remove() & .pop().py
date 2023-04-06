n = int(input())
s = set(map(int, input().split()))

N = int(input())
for _ in range(N):
    c = input().split()
    if len(c)==1: s.pop()
    elif len(c[0])==6: s.remove(int(c[1]))
    elif len(c[0])==7: s.discard(int(c[1]))

print(sum(s))
