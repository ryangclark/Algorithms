#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  max = None

  if len(recipe) != len(ingredients):
    return 0 # 'Ingredient lists don\'t match!'

  for i in recipe:
    try:
      if recipe[i] > ingredients[i]:
        return 0
      if max == None:
        max = ingredients[i] // recipe[i]
        continue
      if ingredients[i] // recipe[i] < max:
        max = ingredients[i] // recipe[i]

    except AttributeError:
      return 'Ingredient lists don\'t match!'

  return max


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
