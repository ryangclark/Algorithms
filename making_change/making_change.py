#!/usr/bin/python

import sys

def making_change(amount, denominations):
  cache = [0] * (amount + 1)
  # seed cache with known value
  cache[0] = 1

  for coin in denominations:
    for higher_amount in range(coin, amount + 1):
      method = higher_amount - coin

      if cache[method]:
        cache[higher_amount] += cache[method]

  return cache[amount]

print(making_change(20, [1, 5, 10, 25, 50]))


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
