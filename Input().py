x,k = list(map(int, input().split()))
p = input()
print(eval(''.join(map(str,[x if _ == 'x' else _ for _ in p])))==k)
