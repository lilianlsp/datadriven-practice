select 
  amount
 from cloud_costs
 group by amount 
 order by amount desc
 limit 3
