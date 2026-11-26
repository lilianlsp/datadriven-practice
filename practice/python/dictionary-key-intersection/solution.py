def dictionary_key_intersection(d1: dict, d2: dict):
  d3 = set(d1.keys())
  d4 = set(d2.keys())
  
  e = d3.intersection(d4)
  
  result = sorted([[k,v] for k, v in d1.items() if k in e])
  return result
