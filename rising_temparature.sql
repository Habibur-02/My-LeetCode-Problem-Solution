select today.id
from Weather as today
join Weather as yesterday
on today.recordDate=yesterday.recordDate + INTERVAL '1 day'
where today.temperature>yesterday.temperature;
