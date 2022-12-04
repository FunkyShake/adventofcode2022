with open('input.txt', 'r') as f:
    ls = [l.strip().split(',') for l in f]

    pairs = 0

    for i in ls:
        (a, b), (x, y) = i[0].split('-'), i[1].split('-')

        if (int(a) <= int(x)) and (int(b) >= int(y)):
            pairs += 1
        elif (int(x) <= int(a)) and (int(y) >= int(b)):
            pairs += 1
        else:
            pass

    print(pairs)
