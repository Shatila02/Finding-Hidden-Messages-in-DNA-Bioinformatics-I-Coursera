import sys


def genome_path(patterns):
    text = patterns[0]
    k = len(patterns[0])
    for i in range(len(patterns) - 1):
        if patterns[i][1:] == patterns[i+1][:k-1]:
            text += patterns[i+1][k-1]
    return text


#patterns = ['ACCGA', 'CCGAA', 'CGAAG', 'GAAGC', 'AAGCT']

"""ACCGA
CCGAA
CGAAG
GAAGC
AAGCT"""
if __name__ == "__main__":
    Input = sys.stdin.readlines()
    patternList = [pattern.strip() for pattern in Input]
    ans = genome_path(patternList)
    print(ans)
