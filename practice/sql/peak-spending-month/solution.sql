select 
  to_char(date_trunc(bill_date, month), 'YYYY-MM') as billing_month,
  sum(amount) as total_spend
from cloud_costs
group by date_trunc(bill_date, month)
order by total_spend desc
limit 1
