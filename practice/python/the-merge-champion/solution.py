def merge_k_sorted(lists: list) -> list:
  result = [] 
  
  for i in lists:
    if isinstance(i, list):
      result.extend(i)
    else:
      result.append(i)
    
  result = sorted(result)
  return result
