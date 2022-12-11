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

with open('input.txt', 'r') as f:
    data = [l.split(' ') for l in f.read().split('\n')]
    visited = [(0,0)]

    y1, x1, y2, x2, = 0, 0, 0, 0

    for ipt in data:
        d, m = ipt[0], int(ipt[1])
        # only really need to track the head
        if m < 2:
            y1, x1 = movement(d, m, y1, x1)
        else:
            for i in range(m):
                # if the head moves more than two spaces from last point
                if d == 'U':
                    if len(range(y1, y2)) == 1:
                        y2, x2 = y1, x1
                        visited.append((y2, x2))
                        y1, x1 = movement(d, m, y1, x1)
                    else:
                        y1, x1 = movement(d, m, y1, x1)
                elif d == 'D':
                    if len(range(y2, y1)) == 1:
                        y2, x2 = y1, x1
                        visited.append((y2, x2))
                        y1, x1 = movement(d, m, y1, x1)
                    else:
                        y1, x1 = movement(d, m, y1, x1)
                elif d == 'L':
                    if len(range(x1, x2)) == 1:
                        y2, x2 = y1, x1
                        visited.append((y2, x2))
                        y1, x1 = movement(d, m, y1, x1)
                    else:
                        y1, x1 = movement(d, m, y1, x1)
                elif d == 'R':
                    if len(range(x2, x1)) == 1:
                        y2, x2 = y1, x1
                        visited.append((y2, x2))
                        y1, x1 = movement(d, m, y1, x1)
                    else:
                        y1, x1 = movement(d, m, y1, x1)
                # then second point should become that last point
    print(len(set(visited)))
