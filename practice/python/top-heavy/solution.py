def inverted_triangle(n: int) -> list[str]:
  result = [] 
  asterisc = '*'
  for i in range(1,n+1):
    result.append(i * asterisc)
    
  final = list(reversed(result))
  return final
