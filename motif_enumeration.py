def motif_enumeration(dna, k, d):
    patterns = []
    kmers = []
    if d == 0:
        for i in dna:
            for j in range(len(i) - k + 1):
                kmers.append(i[j:j+k])
        for kmer in kmers:
            count = []
            for d in dna:
                count.append(approximate_pattern_count(d, kmer, 0))
            if 0 not in count and kmer not in patterns:
                patterns.append(kmer)
    else:
        n = []
        for i in dna:
            for j in range(len(i) - k + 1):
                kmer = i[j:j+k]
                for neighbor in neighbors(kmer, d):
                    n.append(neighbor)
                kmers.append(kmer)
        for pat in n:
            count = []
            for i in dna:
                count.append(approximate_pattern_count(i, pat, d))
            if 0 not in count and pat not in patterns:
                patterns.append(pat)
    return patterns


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


dna = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']
k = 3
d = 1
print(motif_enumeration(dna, k, d))


