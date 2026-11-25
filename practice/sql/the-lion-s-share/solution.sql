select 
  products.category,
  sum(transactions.total_amount) as total_revenue,
  count(distinct transactions.transaction_id) as transaction_count
from products 
join transactions on products.product_id = transactions.product_id
group by products.category
order by total_revenue desc
