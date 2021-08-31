#deque
from collections import deque
a = ['h', 'u', 'n', 'l', 'u', 'l', 'u']
d = deque(a)
print(d)
d.appendleft('python')
print(d)
d.popleft()
print(d)