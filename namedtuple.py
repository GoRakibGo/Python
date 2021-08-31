#namedtuple
from collections import namedtuple
a = namedtuple('courses', 'name, technology')
s = a._make(['artificial intelligence', 'python'])
print(s)