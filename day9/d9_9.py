from numpy import sign as sgn

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

        for i in range(m):
          y1, x1 = movement(d, m, y1, x1)

          if y1 == y2:

            if abs(x1 - x2) >= 2:
              if x2 > x1:
                x2 -= 1
              else:
                x2 += 1
          elif x1 == x2:
            
            if abs(y2 - y1) >= 2:
              if y2 > y1:
                y2 -= 1
              else:
                y2 += 1

          else:
            if abs(x1 - x2) >= 2 or abs(y1 - y2) >=2:
              dx = sgn(x1 - x2)
              dy = sgn(y1 - y2)

              x2 += dx
              y2 += dy



            
          visited.append((y2, x2))


              
print(len(set(visited)))
