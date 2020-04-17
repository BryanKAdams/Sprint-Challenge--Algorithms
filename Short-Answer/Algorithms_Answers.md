#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n). We call n one time


b) O(nlog (n)) We have a for loop that's going through all of n, and we also have a while loop that goes through n logrithmically because it's j *= 2


c) O(n) Bunny ears is recursively called and we're returning bunnies -1 so we're looping through bunnies since the base case is once bunnies is 0.
Or O(bunnies)

## Exercise II
O(n)
 f value is unknown, so we go through the range of the first floor through the nth floor *the highest story of the building* and we pass our function
 the f value that we are looping through the range to get and return f
 if the egg breaks so we know what the value of f is
for f in 1:n
  if egg_breaks(f):
    return f

        o
   O /    o
-- |       o
 _/ \_     o
/-----\      o
| ^_^ |      o
| | | |      *
-------     \#/
