#chainmap
from collections import ChainMap
a = {1: 'learnig things', 2: 'python'}
b = {3: 'ML', 4: 'AI'}
a1 = ChainMap(a,b)
print(a1)