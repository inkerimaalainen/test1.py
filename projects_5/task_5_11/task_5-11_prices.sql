select * from prices
where price between 1000 and 50000; 

select price from prices
where (price between 500 and 7000) and (product_id <= 5); 

select price from prices
where (price < 100) or (price between 60000 and 70000); 