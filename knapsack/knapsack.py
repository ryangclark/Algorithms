#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  pass

def brute_knapsack(items, capacity):
  # items: [Item(index=1, size=42, value=81)]
  # capacity: 100
  # return: {'Value': int, 'Chosen': [ints]}

  cache = {}
  counter = 0

  def recur(index, item_indexes, sum_size, sum_value):
    nonlocal counter
    counter += 1
    cur_item = items[index]
    
    for j in items[index + 1:]:
      if sum_size + j.size <= capacity:
        # note: non-zero-indexes used in n_indexes
        n_indexes = item_indexes + [j.index]
        n_size = sum_size + j.size
        n_value = sum_value + j.value  
        cache[n_value] = n_indexes

        recur(j.index - 1, n_indexes, n_size, n_value)

      else:
        continue

  for i in items:
    recur(i.index - 1, [i.index], i.size, i.value)

  max = 0
  
  for i in cache:
    if int(i) > max:
      max = int(i)
  print(counter)
  return {'Value': max, 'Chosen': cache[max]}

##1 42 81 *
##2 42 42
##3 68 56
##4 68 25
##5 77 14
##6 57 63
##7 17 75 *
##8 19 41 *
##9 94 19
##10 34 12
##
##1, 7, 8

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
