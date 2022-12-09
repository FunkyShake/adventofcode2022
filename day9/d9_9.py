# TODO! Get movements working
# do the correct logic for movement

def movement(d, m, y1, x1):
    if d == 'U'
      yh -= 1
    elif d == 'D':
      yh += 1
    elif d == 'L':
      xh -= 1
    elif d == 'R':
      xh += 1
      
  return yh, xh

with open('input.txt', 'r') as f:
  data = [l.split(' ') for l in f.read().split('\n')]
  
  visited = []
  prev_moves = []
  
  y1, x1, y2, x2, = 0, 0, 0, 0
  
for ipt in data:
  d, m = ipt[0], int(ipt[1])
  prev_moves.append(d)
  
  #insert logic here
  if m < 2: # single movement will never be same as prev direction
    y1, x1 = movement(d, m, y1, x1)
    
  else:
    for i in range(m):
      y1, x1 = movement(d, m, y1, x1)
      #if y2, x2 within 2 logic
      # visited.append((y2, x2))
      
      
      
      
print(len(set(visited)))

      
