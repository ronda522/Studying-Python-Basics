class Super_list(list):
    def __init__(self, list):
        self.list = list

    def __len__(self):
        return print(100)


strs = [1, 2, 3, 5]


super_list = Super_list(str)

super_list.__len__()

super_list.append(5)

print(super_list[0])

print(issubclass(Super_list, list))
