with open('input.txt', 'r') as f:
  ls = [item.split(' ') for item in f.read().split('\n')]
  
  points = 0
  
  for play in ls:
    
    if play[1] == 'X':
      if play[0] == 'A':
        points += 3
      elif play[0] == 'B':
        points += 1
      else:
        points += 2
      
    elif play[1] == 'Y':
      if play[0] == 'A':
        points += 4
      elif play[0] == 'B':
        points += 5
      else:
        points += 6
    
    else:
      if play[0] == 'A':
        points += 8
      elif play[0] == 'B':
        points += 9
      else:
        points += 7
        
  print(points)
