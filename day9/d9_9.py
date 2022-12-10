# TODO! Get movements working
# do the correct logic for movement

def movement(d, m, y, x):
    if d == 'U':
        y -= 1
    elif d == 'D':
        y += 1
    elif d == 'L':
        x -= 1
    elif d == 'R':
        x += 1

    return y, x

with open('test.txt', 'r') as f:
    data = [l.split(' ') for l in f.read().split('\n')]

    visited = []
    prev_moves = []

    y1, x1, y2, x2, = 0, 0, 0, 0

    for ipt in data:
        d, m = ipt[0], int(ipt[1])
        if m < 2:  # single movement will never be same as prev direction
            y1, x1 = movement(d, m, y1, x1)

        else:
            for i in range(m):
                if i == 0:
                    y1, x1 = movement(d, m, y1, x1)
                    # if it's movement is still within 1 of x2, y2

                else:
                    y1, x1 = movement(d, m, y1, x1)
                    y2, x2 = movement(d, m, y2, x2)

                    visited.append((y2,x2))

print(visited)
