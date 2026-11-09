def even_filter(nums: list) -> list:
  result = []
  
  for num in nums:
    if num%2 == 0:
      result.append(num)
  
  return result
