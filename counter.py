#counter
from collections import Counter
a = [1, 1, 2, 3, 2, 2, 4, 5, 7, 5, 6, 3, 4, 9, 8, 0]
c = Counter(a)
print(c)
print(list(c.elements()))
print(c.most_common())
sub = {2:1, 7:1}
print(c.subtract(sub))
print(c.most_common())