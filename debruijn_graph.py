def debruijn_graph(k, text):
    nk = k - 1
    loop = len(text) - nk + 1
    nodes = []
    nodes_1 = []
    graph = {}
    new = set()
    for i in range(loop):
        node = text[i:i+nk]
        nodes.append(node)
    for y in range(len(nodes) - 1):
        n = []
        c = nodes.count(nodes[y])
        if c == 1:
            n.append(nodes[y+1])
        graph[nodes[y]] = n
        if c > 1:
            new.add(nodes[y])
            nodes_1 = list(new)
    for j in nodes_1:
        n = []
        for p in range(len(nodes)):
            if j == nodes[p] and p != len(nodes) - 1:
                n.append(nodes[p+1])
            graph[j] = n
    return graph


k = int(input())
text = input()
r = debruijn_graph(k, text)
for key in r:
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

