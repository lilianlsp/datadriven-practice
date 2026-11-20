select distinct 
  category
from products 
where 
  price between 90 and 200
order by category
