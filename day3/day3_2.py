def chunked(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

with open('input.txt', 'r') as f:
    ls = [l for l in chunked(f.readlines(), 3)]

    total = 0
    for thirds in ls:
        item = sorted(list(set(thirds[0]) & set(thirds[1]) & set(thirds[2])))[::-1]
        if item[0].isupper():
            total+=ord(item[0]) - 38
        else:
            total += ord(item[0]) - 96

    print(total)
