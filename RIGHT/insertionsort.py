def insertion_sort(arr):
  # sort from the the first element but thenn excludes the last index
  for i in range(1,len(arr)):
    # we need the outer loop that starts at the index of the inner loop
    # this is what we do 