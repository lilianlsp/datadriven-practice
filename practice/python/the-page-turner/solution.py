def paginate(pages: list[list]) -> list:
  result = []
  for page in pages:
    if isinstance(page, list):
      result.extend(paginate(page))
    else:
      result.append(page)
  return result
