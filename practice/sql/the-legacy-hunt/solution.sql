select 
  distinct to_char(start_at, 'YYYY-MM-DD')
from data_pipes
where to_char(start_at, 'YYYY-MM-DD')<'2026-05-01'
