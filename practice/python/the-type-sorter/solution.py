def filter_integers(items: list) -> list[int]:
  result = []
  
  for i in items:
    if type(i) is int:
      result.append(i)
      
  return result
