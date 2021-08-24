def distance_between_pattern_and_string(pattern, dna):
    k = len(pattern)
    loop = len(dna[0]) - k + 1
    distance = 0
    for text in dna:
        d = 100000000000000000
        for i in range(loop):
            for kmer in [text[i:i+k]]:
                if d > hamming_distance(pattern, kmer):
                    d = hamming_distance(pattern, kmer)
        distance += d
    return distance


def hamming_distance(p, q):
    count = 0
    for i in range(0, len(p)):
        if p[i] != q[i]:
            count += 1
    return count


dna = ['TTACCTTAAC', 'GATATCTGTC', 'ACGGCGTTCG', 'CCCTAAAGAG', 'CGTCAGAGGT']
pattern = 'AAA'
print(distance_between_pattern_and_string(pattern, dna))
