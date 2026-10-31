def find_missing_ranges(nums: list, lower: int, upper: int) -> list:
  final_list = []
  extended = [lower - 1] + nums + [upper + 1]
  for a, b in zip(extended, extended[1:]):
   result = b-a
   par = []
   if result > 1:
    par.append(a+1)
    par.append(b-1)
    final_list.append(par)

  return final_list
