import collections
import sys
from numba import jit

@jit(cache=True)
def main():
    counts = collections.Counter()
    for line in sys.stdin:
        words = line.lower().split()
        counts.update(words)

    for word, count in counts.most_common():
        print(word, count)

if __name__=='main':
    main()