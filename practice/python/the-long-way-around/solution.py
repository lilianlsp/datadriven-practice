def manual_sort(nums):
  result = [] 
    
  
  while len(nums) > 0:
    lower = min(nums)
    result.append(lower) 
    nums.remove(lower)
  
  return result
      
  
