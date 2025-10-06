my_list = [5, 3, 4]


# sqrting the list
sqrd_list = list(map(lambda item: item ** 2, my_list))

print(sqrd_list)

# sorting the list
tupl_list = [(0, 2), (4, 3), (9, 9), (10, -1)]

sorted_list = list(sorted(tupl_list, key=lambda item: item[1]))

print(sorted_list)
