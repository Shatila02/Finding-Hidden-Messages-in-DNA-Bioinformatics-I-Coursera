import sys


def overlap(patterns):
    lap = {}
    lap1 = {}
    for pattern in patterns:
        lap[pattern] = ''
    for pattern in patterns:
        pat = []
        for i in range(len(patterns)):
            if pattern[1:] == patterns[i][:-1]:
                pat.append(patterns[i])
            lap[pattern] = pat
    for key in lap:
        if lap[key] != []:
            lap1[key] = lap[key]
    return lap1


patterns = []
if __name__ == "__main__":
    I = sys.stdin.readlines()
    patterns = [str(a).strip() for a in I]
d = overlap(patterns)
for key in d:
    for v in d[key]:
        if len(d[key]) == 1:
            print(key + ' -> ' + v)
    if len(d[key]) > 1:
        m = str()
        for i in range(len(d[key]) - 1):
            m = d[key][i] + ',' + d[key][i+1]
        print(key + ' -> ' + m)
