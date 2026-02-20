# big O of n.m(m is number of elements and n is the average nu)
# we know we have limit of 26 characters which brings to time complexity O(m) were m is input given and n is average length of the string cz we have to go through every single characher of the string
# mapping a charcount to list of anagrams
frequ={}
for str in strs:
  # here i have created a hashamap
  # this is gonna make all of our elements count be 0 at each
  count=[0]*26
  for c in  str:
    count[ord(c)-ord("a")]+1
# list can not be keys and also we got chnage it to tuples cz tuples are non mutable
frequ[tuple(count)].append(s)


return frequ.values()