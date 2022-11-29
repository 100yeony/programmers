with main as (
select *, left(product_code,2) as category
from product
) select category, count(product_id) as products
from main
group by category