#adding elements to an array
import array as arr
a = arr.array('d', [2.3, 5.4, 7.2, 9.1])
a.append(3.6)
print('Array a =', a)
a.extend([1.2, 8.5, 0.1])
print('Array b =', a)
a.insert(2, 0.5)
print('Array c =', a)
print('Sorted array =', sorted(a))