with open('input.txt', 'r') as f:
  ls = sorted(sum(map(int, item.split())) for item in f.read().split('\n\n'))[::-1]
  
  print(ls[0])
  print(sum(ls[:3]))
