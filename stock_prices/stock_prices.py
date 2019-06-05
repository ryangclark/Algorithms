#!/usr/bin/python

import argparse

def find_max_profit(prices):
  if not type(prices) == type([]):
    return 'Input must be type list'
  
  if len(prices) < 2:
    return 'Input must be list with minimum length of 2'

  max = prices[1] - prices[0]

  for index, item in enumerate(prices):
    for i in prices[index + 1:]:
      if  i - item > max:
        max = i - item
        print('item', item, 'i', i)
       
  return max

print(find_max_profit([100]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
