def gen(num, max_num):
    i = 17
    for _ in range(max_num):
        yield num**i
        i += 27


f = gen(2, 50)
for el in f:
    print(el)
