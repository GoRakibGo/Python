#array concatination
import array as arr
a = arr.array('d', [4.1, 6.3, 9.2, 5.0, 1.3, 2.4])
b = arr.array('d', [0.3, 0.1, 2.7, 8.5, 7.2])
c = arr.array('d')
c = a+b
print('Array c =', c)
print('sorted array =', sorted(c))