import random


def cycle(graph):
    node = random.choice(list(graph))
    li = [node]
    for i in range(10):
        node_2 = 0
        if len(graph[node]) > 1:
            node_2 = random.choice(graph[node])
            if node_2 not in li:
                li.append(node_2)
            else:
                io = graph[node].remove(node_2)
                print(io)
                node_2 = random.choice(io)
        else:
            node_2 = graph[node][0]
            li.append(node_2)
        node = node_2
    print('l', li)
    """for i in li:
            c = li.count(i)
            print('c', c)
            if c > 1:
                node = graph[node][0]
                print('hi', node)"""



g = {0: [3], 1: [0], 2: [1, 6], 3: [2], 4: [2], 5: [4], 6: [5, 8], 7: [9], 8: [7], 9: [6]}
cycle(g)
