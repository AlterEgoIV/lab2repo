array = [5, 100, 7, 20, 1]

max_number = 0

for x in range(0, len(array)):
  if array[x] > max_number:
    max_number = array[x]

print "The maximum number in array is %d" % max_number


