with open('input.txt', 'r') as f:
  ls = [item.split(' ') for item in f.read().split('\n')]
  
  points1 = 0
  points2 = 0
  
  for play in ls:
    
    if play[1] == 'X':
      points1 += 1
      
      if play[0] == 'C':
        points1 += 6
        points2 += 2
      elif play[0] == 'A':
        points1 += 3
        points2 += 3
      else:
        points2 += 1
      
    elif play[1] == 'Y':
      points1 += 2
      points2 += 3
      
      if play[0] == 'A':
        points1 += 6
        points2 += 1
      elif play[0] == 'B':
        points1 += 3
        points2 += 2
      else:
        points2 += 3
    
    else:
      points1 += 3
      points2 += 6
      
      if play[0] == 'B':
        points1 += 6
        points2 += 3
      elif play[0] == 'C':
        points1 += 3
        points2 += 1
      else:
        points2 += 2
      
  print(points1, points2)
