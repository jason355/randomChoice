array = [[0] * 2 for k in range(10)]

j = 0

for i in range(10):
    array[i][0] = i+1
    array[i][1] = i
print(array)

loc = 10
number = 12

while loc != array[j]:
    if j + 1 == len(array):
        array[j][1] = loc
        break
    j += 1
print(array)