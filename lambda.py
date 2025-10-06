some_list = ['a', 'b', 'b', 'c', 'd', 'm', 'n', 'n']


# creates
dublicates = list(
    set(
        [item for item in some_list if some_list.count(item) > 1]
    )
)

print(dublicates)
