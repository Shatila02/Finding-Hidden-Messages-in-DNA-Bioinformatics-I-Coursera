def frequent_mismatches_rc(s,k,d):
    counts = {}
    for i in range(len(s)-k+1):
        for sub in [s[i:i+k], reverse_complement(s[i:i+k])]:
            for neighbor in neighbors(sub, d):
                if neighbor not in counts:
                    counts[neighbor] = 0
                counts[neighbor] += 1
    m = max(counts.values())
    return [kmer for kmer in counts if counts[kmer] == m]


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


f = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d = 1
print(frequent_mismatches_rc(f, k, d))
