a = [1, 2, 3, 3, 4]

i = iter(a)
while True:
    try:
        c1 = next(i)
    except StopIteration:
        break
    j = iter(a)
    while True:
        try:
            c2 = next(j)
            print(c1, c2)
            if c1 == c2:
                print("equivalent", c1, c2)
        except StopIteration:
            break