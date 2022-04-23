for a in range(1, 401):
    for b in range(1, 401):
        c = 400 -a -b
        if (a**2 + b**2 == c ** 2):
            if ((a < b) and (b < c) ):
                print("{} {} {}".format(a, b, c))
                print("{}".format(a * b * c))