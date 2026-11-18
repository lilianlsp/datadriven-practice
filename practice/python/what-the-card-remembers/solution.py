def merge_holds(holds):
  result = {}
  for i in holds:
    result.setdefault(i['card'], []).append([i['start'], i['end']])
  
  merged_result = {}
  for card, intervals in result.items():
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
      last = merged[-1]
      if start <= last[1]:
        last[1] = max(last[1], end)
      else:
        merged.append([start, end])
    merged_result[card] = merged
  
  return merged_result
