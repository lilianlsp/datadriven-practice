def chunk_list(records, n):
  return [records[i:i + n] for i in range(0,len(records), n)]
