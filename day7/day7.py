# TODO: 
# add dictionary items to previous dictionary values
#   possibly another loop

import re

with open('input.txt', 'r') as f:

    d = {}
    wkdir = ''
    dirs = []

    for l in f.read().split('\n'):

        if l[:5] == '$ cd ':
            a, b = l[:5], l[5:]
            if b != '..':
                dirs.append(b+'/')
                wkdir += b+'/'
                d.setdefault(wkdir, 0)
            else:
                wkdir = wkdir[:-len(dirs[-1])]
                dirs.pop()
    
        elif l == '$ ls':
            pass
        
        else:
            if l[0].isdigit():
                d[wkdir] += int(re.search(r'\d+', l).group())

    for item in d:
        if d[item] < 100000:
            print(item, d[item])

        
