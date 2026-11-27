select 
  100*(cast(count(distinct content_views.user_id) as numeric)/cast(count(distinct users.user_id) as numeric)) as view_pct
from users
left join content_views on users.user_id = content_views.user_id
