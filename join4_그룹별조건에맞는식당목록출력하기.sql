select member_name, review_text, left(review_date,10) as review_date
from rest_review a
join member_profile b on a.member_id=b.member_id
where a.member_id in (
    with main as (
    SELECT member_name,review_text,review_date, count(review_id) as cnt, b.member_id
    from rest_review a
    join member_profile b on a.member_id = b.member_id
    group by a.member_id
    order by cnt desc
        )
        select member_id
        from main c
        where c.cnt = (
            select max(cnt)
            from main
        )
)
order by review_date, review_text