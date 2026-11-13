def flatten(nested):
  result = []

  for i in nested:
    if isinstance(i, list):
      result.extend(i)
    else:
      result.append(i)

  return result
