#looping through an array
import array as arr
a = arr.array('d', [3.4, 2.1, 4.9, 5.3, 6.0, 8.7])
print('All values of array a')
#for loop
for x in a:
    print(x)

#while loop
b = arr.array('d', [4.4, 5.7, 8.0, 9.9, 0.3, 3.1])
temp = 0
print('All values of array b')
while temp<len(b):
    print(b[temp])
    temp += 1