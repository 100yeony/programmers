with main as (
select product_id, sum(amount) as total
from food_order
where produce_date between '2022-05-01' and '2022-05-31'
group by product_id
    ) select a.product_id, b.product_name, total*price as total_sales
    from main a
    inner join food_product b on a.product_id=b.product_id
    order by total_sales desc, product_id