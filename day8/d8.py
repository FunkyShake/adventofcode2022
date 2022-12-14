import numpy as np

def north(grid, pos_x, pos_y):
    n = [grid[i, pos_y] for i in reversed(range(pos_x))]
    return any(grid[pos_x, pos_y] <= item for item in n)

def south(grid, pos_x, pos_y):
    s = [grid[i, pos_y] for i in range(pos_x + 1, len(grid))]
    return any(grid[pos_x, pos_y] <= item for item in s)

def west(grid, pos_x, pos_y):
    w = [grid[pos_x, i] for i in reversed(range(pos_y))]
    return any(grid[pos_x, pos_y] <= item for item in w)

def east(grid, pos_x, pos_y):
    e = [grid[pos_x, i] for i in range(pos_y + 1, len(grid))]
    print(e)
    return any(grid[pos_x, pos_y] <= item for item in e)


with open('input.txt', 'r') as f:
    arr = np.array([[int(letter) for letter in list(l)] for l in f.read().split('\n')])

    visible = (len(arr) * len(arr))

    for x in range(1, len(arr) - 1):
        for y in range(1, len(arr) - 1):

            if north(arr, x, y):
                if south(arr, x, y):
                    if west(arr, x, y):
                        if east(arr, x, y):
                            visible -= 1
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue

    print(visible)
