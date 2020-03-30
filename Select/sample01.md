# 题目
一张表的结构如下  
mysql> select * from student;  
+------+---------+--------+
| name | subject | score |
+------+---------+--------+
| 张三 | 数学    |     80 |
| 张三 | 语文    |     53 |
| 张三 | 英语    |     59 |
| 李四 | 数学    |     55 |
| 李四 | 语文    |     56 |
| 李四 | 英语    |     50 |
| 王五 | 数学    |    100 |
| 王五 | 语文    |     90 |
+------+---------+--------+
CREATE TABLE studnet(name varchar(32) not null, subject varchar(32) not null, score int(3) not null)
```
## 问题1：使用一个查询语句查询出不及格科目大于或等于2科的学生的平均分（所有科目的平均分)
```
SELECT name, AVG(score), SUM(score<60) as cnt FROM student GROUP BY name HAVING cnt >= 0
```
## 备注
使用count统计。count永远是统计的所有行
使用sum统计，先统计所有人的平均分，再筛选
## 问题2：查询每个学生最大分数的科目及分数
正解1：使用where子查询，先找到每个学生的最大分数，再根据分数刷新出记录
```
SELECT * FROM student WHERE socre IN (SELECT MAX(score) FROM student GROUP BY name)
```
正解2：FROM子查询，先排序，在group by拿到第一个，即最大分数的那条记录
```
SELECT * FROM (SELECT * FROM student ORDER BY score DESC) AS tmp GROUP BY name;
```
