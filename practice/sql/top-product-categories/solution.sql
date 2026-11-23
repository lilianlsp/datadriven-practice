with ranked_category as (select 
  category,
  count(distinct transaction_id) as txn_count,
  dense_rank() over(
    order by count(distinct transaction_id) desc) as rnk
from products
join transactions on products.product_id = transactions.product_id
where products.rating >=3.0
and products.rating is not null
group by category)
select * from ranked_category
where rnk <=3
