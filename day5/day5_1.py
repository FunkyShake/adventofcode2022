import re

# i couldn't quite figure out how to make an array plus instructions
# out of the input so here's a hand-jammed array
data1 = [
  ['S', 'L', 'W'], ['J','T','N','Q'], ['S','C','H','F','J'], 
  ['T','R','M','W','N','G','B'],['T','R','L','S','D','H','Q','B'],
  ['M','J','B','V','F','H','R','L'], ['D','W','R','N','J','M'], 
  ['B','Z','T','F','H','N','D','J'], ['H','L','Q','N','B','F','T']
]

# let's face it, it's a struggle for some of us
data2 = [
  ['S', 'L', 'W'], ['J','T','N','Q'], ['S','C','H','F','J'], 
  ['T','R','M','W','N','G','B'],['T','R','L','S','D','H','Q','B'],
  ['M','J','B','V','F','H','R','L'], ['D','W','R','N','J','M'], 
  ['B','Z','T','F','H','N','D','J'], ['H','L','Q','N','B','F','T']
]

with open('input.txt', 'r') as f:
  
  ls = [re.findall(r'\d+', l) for l in f.readlines()]
  
  for i in ls:
    for times in range(1, int(i[0])+1):
      data1[int(i[2])-1].append(data1[int(i[1])-1].pop())

    data2[int(i[2])-1] = data2[int(i[2])-1] + data2[int(i[1])-1][-int(i[0]):]
    data2[int(i[1])-1] = data2[int(i[1])-1][:-int(i[0])]
  
  print(''.join([a[-1] for a in data1]), ''.join([b[-1] for b in data2]))
