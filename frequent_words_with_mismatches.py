def frequent_words_with_mismatches(text, k, d):
    frequent_pattern = []
    neighbor_hood = []
    loop = len(text) - k + 1
    index = []
    count = []
    neighbor_hood_array = []
    for i in range(loop):
        p = text[i:i+k]
        neighbor_hood.append(neighbors(p, d))
    for n in neighbor_hood:
        for s in n:
            neighbor_hood_array.append(s)
    loop_1 = len(neighbor_hood_array)
    for j in range(loop_1):
        pattern = neighbor_hood_array[j]
        index.append(pattern_to_number(pattern))
        count.append(1)
    index.sort()
    for t in range(loop_1 - 1):
        if index[t] == index[t+1]:
            count[t + 1] = count[t] + 1
    m = max(count)
    for i in range(loop_1):
        if count[i] == m:
            pattern = number_to_pattern(index[i], k)
            frequent_pattern.append(pattern)
    return set(frequent_pattern)


def neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    neighbor_hood = []
    first = pattern[1:]
    suffix_neighbors = neighbors(first, d)
    for s in suffix_neighbors:
        if hamming_distance(first, s) < d:
            for x in 'ACGT':
                n = x + s
                neighbor_hood.append(n)
        else:
            n = pattern[0] + s
            neighbor_hood.append(n)
    return neighbor_hood


def hamming_distance(p, q):
    count = 0
    for i in range(0, len(p)):
        if p[i] != q[i]:
            count += 1
    return count


def pattern_to_number(pattern):
    if len(pattern) == 0:
        return 0
    symbol = pattern[len(pattern) - 1]
    prefix = pattern[:-1]
    d = {"A": 0, "C": 1, "G": 2, "T": 3}
    a = int(d[symbol])
    result = 4 * pattern_to_number(prefix) + a
    return result


def number_to_pattern(index, k):
    d = {"0": "A", "1": "C", "2": "G", "3": "T"}
    if k == 1:
        return d[str(index)]
    else:
        prefixindex = index // 4
        r = str(index % 4)
        symbol = d[r]
        prefixpattern = number_to_pattern(prefixindex, k - 1)
        return prefixpattern + symbol


genome = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
print(frequent_words_with_mismatches(genome, 4, 1))
