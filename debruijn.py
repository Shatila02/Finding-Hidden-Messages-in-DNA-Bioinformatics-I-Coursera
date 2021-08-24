import sys


def debruijn(patterns):
    prefix = []
    graph = {}
    for i in range(len(patterns)):
        prefix.append(patterns[i][:-1])
    for key in prefix:
        graph[key] = []
    for key in graph:
        suf = []
        for i in range(len(patterns)):
            if key == patterns[i][:-1]:
                suf.append(patterns[i][1:])
                suf.sort()
                graph[key] = suf
    return graph


text = []
if __name__ == '__main__':
    Input = sys.stdin.readlines()
    text = [str(a).strip() for a in Input]
r = debruijn(text)
for key in sorted(r):
    for v in r[key]:
        if len(r[key]) == 1:
            print(key + ' -> ' + v)
    if len(r[key]) > 1:
        m = str()
        for i in range(1):
            m = r[key][i]
            j = 0
            while j != len(r[key]) - 1:
                m += ',' + r[key][j+1]
                j += 1
        print(key + ' -> ' + m)
