with open('input.txt', 'r') as f:
  ls = [item.split(' ') for item in f.read().split('\n')]
  
  points = 0
  
  for play in ls:
    
    if play[1] == 'X':
      points += 1
      if play[0] == 'C':
        points += 6
      elif play[0] == 'A':
        points += 3
      else:
        pass
      
    elif play[1] == 'Y':
      points += 2
      if play[0] == 'A':
        points += 6
      elif play[0] == 'B':
        points += 3
      else:
        pass
    
    else:
      points += 3
      if play[0] == 'B':
        points += 6
      elif play[0] == 'C':
        points += 3
      else:
        pass
      
  print(points)
