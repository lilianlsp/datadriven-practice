def flatten(feed: list) -> list:
  all_ids = []
  for entry in feed:
    if isinstance(entry, list):
      all_ids.extend(flatten(entry))
    else:
      all_ids.append(entry)
      
  return all_ids
