with open('input.txt', 'r') as f:
  ls = [item.strip() for item in f]
  
  biggest = 0
  adder = 0
  
  for i in ls:
    if i != '':
      adder += int(i)
      
    else:
        if adder > biggest:
            biggest = adder
            adder = 0
        else:
            adder = 0
  
  print(biggest)
