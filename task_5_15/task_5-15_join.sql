select
  p.name as "Название товара",
  pr.price as "Цена"
from products p
join prices pr on p.id = pr.product_id;

