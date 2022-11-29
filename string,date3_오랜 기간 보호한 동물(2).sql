with main as (
SELECT a.animal_id, a.datetime as adate, b.datetime, datediff(b.datetime, a.datetime) as diff,a.name
from animal_ins a
inner join animal_outs b on (a.ANIMAL_ID = b.animal_id)
order by diff desc
limit 2
    ) select animal_id, name
    from main