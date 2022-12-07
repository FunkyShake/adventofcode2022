import re

with open('input.txt', 'r') as f:

    d = {}
    wkdir = ''
    dirs = []
    wkdirs = []

    for l in f.read().split('\n'):
        
        # if input is cd
        if l[:5] == '$ cd ':
            a, b = l[:5], l[5:]
            
            # cd to a directory
            if b != '..':
                dirs.append(b+'/')
                wkdir += b+'/'
                wkdirs.append(wkdir) 
                d.setdefault(wkdir, 0) # setting a blank dictionary entry
            
            # go back to parent dir
            else:
                wkdir = wkdir[:-len(dirs[-1])]
                dirs.pop()
        
        # if ls
        elif l == '$ ls':
            pass
        
        # add the value to the dictionary entry
        else:
            if l[0].isdigit():
                d[wkdir] += int(re.search(r'\d+', l).group())
                
                # add it to all previous dictionary entries
                for prevdir in wkdirs:
                    if prevdir in wkdir and prevdir != wkdir:
                        #print(prevdir, wkdir)
                        d[prevdir] += int(re.search(r'\d+', l).group())
                        

    result = 0
    for item in d:
        if d[item] < 100000:
            result += d[item]

    print(result)

        
