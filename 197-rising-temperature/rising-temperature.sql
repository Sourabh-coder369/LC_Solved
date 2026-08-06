# Write your MySQL query statement below
WITH P AS (
    SELECT id,recordDate,temperature,LAG(recordDate) over(order by recordDate) AS prevDate
    FROM Weather
),
T AS (
    SELECT * FROM P WHERE DATEDIFF(recordDate,prevDate)=1
)

SELECT t1.id
FROM T AS t1 JOIN weather as t2 ON (t1.prevDate=t2.recordDate) AND (t1.temperature>t2.temperature)