import numpy as np

def north(grid, pos_x, pos_y):
    n = [grid[i, pos_y] for i in reversed(range(pos_x))]
    counter = 0
    for item in n:
        if item < grid[pos_x, pos_y]:
            counter += 1
        else:
            counter += 1
            break
    return counter

def south(grid, pos_x, pos_y):
    s = [grid[i, pos_y] for i in range(pos_x + 1, len(grid))]
    counter = 0
    for item in s:
        if item < grid[pos_x, pos_y]:
            counter += 1
        else:
            counter += 1
            break
    return counter

def west(grid, pos_x, pos_y):
    w = [grid[pos_x, i] for i in reversed(range(pos_y))]
    counter = 0
    for item in w:
        if item < grid[pos_x, pos_y]:
            counter += 1
        else:
            counter += 1
            break
    return counter
  
def east(grid, pos_x, pos_y):
    e = [grid[pos_x, i] for i in range(pos_y + 1, len(grid))]
    counter = 0
    for item in e:
        if item < grid[pos_x, pos_y]:
            counter += 1
        else:
            counter += 1
            break
    return counter

with open('input.txt', 'r') as f:
    arr = np.array([[int(letter) for letter in list(l)] for l in f.read().split('\n')])
    highest = 0

    for x in range(1, len(arr) - 1):
        for y in range(1, len(arr) - 1):

            a = north(arr, x, y)
            b = south(arr, x, y)
            c = west(arr, x, y)
            d = east(arr, x, y)

            print(a, b, c, d)
            if (a * b * c * d) > highest:
                highest = a * b * c * d
            else:
                pass

    print(highest)
