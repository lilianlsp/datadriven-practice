def flatten_generator(nested: list) -> list:
  flatten =[]
  for i in nested:
    if isinstance(i,list):
      flatten.extend(flatten_generator(i))
    else:
      flatten.append(i)
       
  return flatten
