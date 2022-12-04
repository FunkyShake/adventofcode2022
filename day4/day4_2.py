with open('input.txt', 'r') as f:
    ls = [l.strip().split(',') for l in f]

    overlaps = 0

    for i in ls:
        (a, b), (x, y) = i[0].split('-'), i[1].split('-')

        if (int(b) >= int(x)) and (int(a) <= int(x)):
            overlaps += 1
        elif (int(y) >= int(a)) and (int(x) <= int(a)):
            overlaps += 1
        else:
            pass

    print(overlaps)
