def remove_dupes(items):
  result = []
  
  for i in items:
    if i in result:
      None
    else:
      result.append(i)
  return result
