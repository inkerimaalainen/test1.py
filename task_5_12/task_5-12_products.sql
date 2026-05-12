select 
count(*) as number_of_products,
category
from products
group by category; 

select 
count(*) as number_of_products,
category
from products
group by category
order by number_of_products desc; 