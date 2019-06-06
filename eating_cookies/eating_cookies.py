#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n == 0 or n == 1:
    return 1

  one_prev = 2
  two_prev = 1
  thr_prev = 1

  i = 2
  while i < n:
    one_prev, two_prev, thr_prev = one_prev + two_prev + thr_prev, one_prev, two_prev
    i += 1

  return one_prev


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

