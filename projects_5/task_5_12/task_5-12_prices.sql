select
count(*) as number_of_prices,
product_id
from prices
group by product_id
order by product_id; 

select
avg(price) as average_price,
product_id
from prices
group by product_id
order by product_id;

select
min(price) as minimum_price,
product_id
from prices
group by product_id
order by product_id;

select
max(price) as maximum_price,
product_id
from prices
group by product_id
order by product_id;