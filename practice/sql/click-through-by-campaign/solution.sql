select 
  ad_campaign,
  count(distinct impression_id) as total_impressions,
  round(100*cast(count(distinct case when clicked = 1 then impression_id end) as decimal)/
    count(distinct impression_id),2) as clicked_pct,
  round(100*cast(count(distinct case when clicked = 0 then impression_id end) as decimal)/
    count(distinct impression_id),2) as not_clicked_pct
from ad_impressions
group by ad_campaign
