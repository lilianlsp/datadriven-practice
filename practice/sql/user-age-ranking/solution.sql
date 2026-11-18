select 
  user_id,
  dense_rank() over(order by age_bucket desc) as rank
from users
