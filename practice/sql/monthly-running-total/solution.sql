with montly_information as(select 
  product_id,
  to_char(date_trunc(transaction_date, month), 'YYYY-MM') as month,
  sum(total_amount) as monthly_total
from transactions
where product_id is not null
group by 1,2)
select 
  product_id,
  month,
  monthly_total,
  sum(monthly_total) over(partition by product_id order by month asc 
                          rows between unbounded preceding and current row) as cumulative_total
from montly_information
