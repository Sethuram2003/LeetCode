# Write your MySQL query statement below
-- select round(sum(tiv_2016),2) as tiv_2016 from Insurance group by tiv_2015 having ;
-- select * from insurance where tiv_2015 in (select tiv_2015 from insurance group by tiv_2015) and pid in (select pid from insurance group by lat,lon)

select round(sum(tiv_2016),2) as tiv_2016 from insurance where pid in
(select pid from insurance group by lat,lon having count(*)=1) and tiv_2015 in
(select tiv_2015 from insurance group by tiv_2015 having count(*)>1)