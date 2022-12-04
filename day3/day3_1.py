with open('input.txt', 'r') as f:
    ls1 = [list(set(item[:(len(item) // 2)]) & set(item[(len(item) // 2):])) for
          item in f.read().split()]

    total = 0

    for item in ls1:
        if item[0].isupper():
            total+=ord(item[0]) - 38
        else:
            total += ord(item[0]) - 96

    print(total)
