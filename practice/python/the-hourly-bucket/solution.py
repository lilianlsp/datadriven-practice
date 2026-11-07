def group_by_hour(events):
  group = {}
  
  for event in events:
    group.setdefault(event["ts"][0:13], []).append(event["type"])

  return group
