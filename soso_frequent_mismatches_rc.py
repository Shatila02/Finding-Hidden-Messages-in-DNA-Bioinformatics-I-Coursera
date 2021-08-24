def reverse(pattern):
    rev = ''
    for char in pattern:
        rev = char + rev
    return rev


def complement(pattern):
    d = {'A': "T", 'T': 'A', 'G': 'C', 'C': 'G'}
    com = ''
    for char in pattern:
        com += d.get(char)
    return com


def reverse_complement(pattern):
    a = reverse(pattern)
    b = complement(a)
    return b


def neighbors(pattern, d):
    if d == 0:
        return [pattern]
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


def approximate_pattern_count(text, pat, di):
    k = len(pat)
    loop = len(text) - k + 1
    count = 0
    for i in range(loop):
        lst = text[i:i+k]
        s = hamming_distance(pat, lst)
        if s <= di:
            count += 1
    return count


def frequent_mismatches_rc(text, k, d):
    loop = len(text) - k + 1
    frequent = []
    coun = {}
    lit2 = []
    lit = []
    n = []
    m = 0
    for i in range(loop):
        pattern = text[i:i+k]
        lit1 = neighbors(pattern, d)
        lit2.append(lit1)
    for i in lit2:
        for j in i:
            lit.append(j)
    lit.sort()
    for i in range(len(lit)):
        coun1 = approximate_pattern_count(text, lit[i], d)
        coun2 = approximate_pattern_count(text, reverse_complement(lit[i]), d)
        coun[i] = coun1 + coun2
    for i in coun:
        n.append(coun[i])
    m = max(n)
    for i in coun:
        if coun[i] == m:
            frequent.append(lit[i])
    return set(frequent)


f = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d = 1
print(frequent_mismatches_rc(f, k, d))
