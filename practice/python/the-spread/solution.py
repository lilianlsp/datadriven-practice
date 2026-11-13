def the_spread(nums: list[float]):
  x_sum = 0
  x_sum2 = 0
  
  if len(nums) >= 2:
    for i in nums:
      x_sum = x_sum + i
    
    x_bar = x_sum/len(nums) 
    for i in nums:
      x_sum2 = x_sum2 + (i - x_bar) ** 2
    return round(x_sum2/(len(nums)-1),2)
  else: 
    return 0.0
  
