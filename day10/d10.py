with open('input.txt', 'r') as f:
    data = [l.split(' ') for l in f.read().split('\n')]
    x = 1
    cycle = 0
    signal_poi = [20, 60, 100, 140, 180, 220]
    signals = []

    for inst in data:
        if inst[0] == 'noop':
            cycle += 1
            if cycle in signal_poi:
                signals.append(x * cycle)
        else:
            cycle += 1
            if cycle in signal_poi:
                signals.append(x * cycle)
                cycle += 1
                x += int(inst[1])
            else:
                cycle += 1
                if cycle in signal_poi:
                    signals.append(x * cycle)
                    x += int(inst[1])
                else:
                    x += int(inst[1])

    print(sum(signals))
