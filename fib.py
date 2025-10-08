def fib(num):
    fst_number = 0
    scn_number = 1

    for i in range(num):
        yield fst_number
        temp = fst_number
        fst_number = scn_number
        scn_number = temp + scn_number


for x in fib(100):
    print(x)
