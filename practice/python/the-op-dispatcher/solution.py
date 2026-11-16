def apply_transform(records, op_name):
  
  for record in records:
    if op_name == 'double':
      record['result'] = 2 * record['value']
    elif op_name == 'abs':
      record['result'] = abs(record['value'])
    elif op_name == 'square':
      record['result'] = record['value'] * record['value']
    elif op_name == 'upper':
      record['result'] = record['value'].upper()
    else:
      record['result'] = record['value'].lower()
  return records
