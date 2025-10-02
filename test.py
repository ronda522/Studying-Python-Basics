list = [12, 47, 83, 5, 91, 34, 76, 29, 55, 100,
        62, 8, 39, 71, 18, 95, 41, 22, 68, 3,
        11, 59, 25, 87, 36, 99, 14, 65, 49, 7,
        92, 28, 53, 80, 16, 74, 33, 44, 9, 63,
        27, 85, 19, 51, 6, 97, 32, 58, 73, 21]

def Highest_even(list):
    even_args = []
    for args in list:
        if args % 2 == 0:
            even_args.append(args)
    return max(even_args)

print(Highest_even(list))