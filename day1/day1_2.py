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
            top.append(biggest)
            adder = 0
        else:
            adder = 0
  top.append(adder)
  
  print(biggest, sum(sorted(top[-3:])))
