with main as (
SELECT j.shipment_id, j.flavor, sum(j.total_order) + f.total_order as total
from july j
left join first_half f on j.shipment_id=f.shipment_id
group by flavor
order by total desc
    ) select flavor
    from main
    limit 3