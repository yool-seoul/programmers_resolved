SELECT HOUR(datetime) as HOUR, count(*) from animal_outs 
group by HOUR
having HOUR between 9 and 19
order by HOUR