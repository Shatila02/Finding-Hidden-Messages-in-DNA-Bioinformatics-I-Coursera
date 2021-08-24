def median_string(dna, k):
    distance = 10**100
    median = ''
    for i in range(0, 4**k -1):
        pattern = number_to_pattern(i, k)
        if distance > distance_between_pattern_and_string(pattern, dna):
            distance = distance_between_pattern_and_string(pattern, dna)
            median = pattern
    return median


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


dna = [
'CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC',
'GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC',
'GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG'
]
k = 7
print(median_string(dna, k))
