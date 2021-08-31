#removing elements of an array
import array as arr
a = arr.array('d', [4.4, 5.7, 8.0, 9.9, 0.3, 3.1])
print(a)
print('poping last element', a.pop())
print('poping 4th element', a.pop(3))
a.remove(4.4)
print('sorted array =', sorted(a))
