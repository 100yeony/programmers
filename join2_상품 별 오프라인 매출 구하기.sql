with main as (
select product_id, sum(sales_amount) as cnt
from offline_sale
group by product_id
) select product_code, cnt*price as sales
from product a 
inner join main b on a.product_id=b.product_id
order by sales desc, a.product_code asc