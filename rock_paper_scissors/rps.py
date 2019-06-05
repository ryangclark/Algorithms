#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  plays = ['rock', 'paper', 'scissors']
  plays_list = [[]]

  for i in range(n):
    acc = []
    for index, item in enumerate(plays_list):
      for j in plays:
        acc.append(item + [j])
    plays_list = acc
    
  return plays_list


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

