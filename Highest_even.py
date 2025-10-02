list = [7, 12, 3, 18, 5, 1, 14, 9, 19, 6]

def Highest_even(list):
    even_args = []
    for args in list:
        if args % 2 == 0:
            even_args.append(args)
            max_even_arg = max(even_args)
    return max_even_arg

print(Highest_even(list))