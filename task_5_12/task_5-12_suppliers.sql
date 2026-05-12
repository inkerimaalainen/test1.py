select 
count(*) as number_of_suppliers,
product_id
from suppliers
group by product_id
order by product_id;