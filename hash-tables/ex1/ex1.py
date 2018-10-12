def get_indices_of_item_weights(weights, limit):
  ht = {}
  for i in range(len(weights)):
    weight = weights[i]
    if (weight not in ht):
      ht[weight] = i
    if limit - weight in ht and ht[limit - weight] is not i:
      return (i, ht[limit - weight])
  return()

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  print(get_indices_of_item_weights([4, 6, 10, 15, 16], 21))