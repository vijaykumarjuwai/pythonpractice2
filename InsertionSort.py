import random
arr = random.sample(xrange(1, 101), 10)

def insertionsort( aList ):
  for i in range( 1, len( aList ) ):
    tmp = aList[i]
    k = i
    while k > 0 and tmp < aList[k - 1]:
        aList[k] = aList[k - 1]
        k -= 1
    aList[k] = tmp

insertionsort(arr)
print   " ".join(map(str, arr))