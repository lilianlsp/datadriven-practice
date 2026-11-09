with ranked as (select
  *, 
  row_number() 
    over(partition by user_id
         order by transaction_date asc) as rn
from transactions)
select 
  user_id,
  total_amount,
  transaction_date
from ranked
where rn = 2
