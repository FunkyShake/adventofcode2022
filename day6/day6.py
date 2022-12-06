with open('input.txt', 'r') as f:
    data = f.read()

    for i in range(len(data)):
        if len(set(data[i:i+4])) == 4:
            print('part 1 ',i+4)
            break

    for j in range(len(data)):
        if len(set(data[j:j+14])) == 14:
            print('part 2 ',j+14)
            break
