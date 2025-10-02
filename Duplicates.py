args = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

args = sorted(args)

for dub in range(len(args) - 1):
    if args[dub] == args[dub + 1]:
        print(args[dub])
    