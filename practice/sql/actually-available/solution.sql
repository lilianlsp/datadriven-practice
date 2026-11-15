select count(distinct product_id) as in_stock_count from products
where in_stock = 1
