import itertools

s = "abc"
for i in range(4):
    perms = itertools.permutations(s, i)

    for perm in perms:
        print(''.join(perm))
        print(type(perm))
        a = ''.join(perm)
        print(type(a))