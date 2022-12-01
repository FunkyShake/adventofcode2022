with open('input.txt', 'r') as f:
  ls = [item.strip() for item in f]
  
  biggest = 0
  adder = 0
  top = []
  
  for i in ls:
    if i != '':
      adder += int(i)
      
    else:
        top.append(adder)
        if adder > biggest:
            biggest = adder
            adder = 0
        else:
            adder = 0
  top.append(adder)
  top = sorted(top) # couldn't get this to work in the print statement
  print(biggest, sum(top[-3:]))
