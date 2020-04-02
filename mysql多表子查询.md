# mysql多表子查询

## 1 题目描述

有三张数据表，结构如下：

人员表：人员姓名，人员id

销售表：人员id，时间，销售金额

花费表：人员id，时间，花费金额

写一条SQL语句，完成下面的统计结果：

**人员姓名，总花费，总销售**

注意：需要使用子查询，三张表关联不行，会出现重复数据。

## 2 构造数据

### 2.1 创建人员表

```mysql
create  table user(id int,name varchar(20));
insert into user values(1, 'A');
insert into user values(2, 'B');
```

### 2.2 创建销售表

```mysql
create  table sale(userid int,sale_time date, sale_money double);
insert into sale values(1, '2019-2-21', 1000);
insert into sale values(1, '2019-2-22', 600);
insert into sale values(2, '2019-2-23', 1500);
insert into sale values(2, '2019-2-24', 800);
```

### 2.3 创建话费表

```mysql
create  table cost(userid int,cost_time date, cost_money double);
insert into cost values(1, '2019-2-23', 900);
insert into cost values(1, '2019-2-24', 800);
insert into cost values(2, '2019-2-25', 1400);
insert into cost values(2, '2019-2-26', 1600);
```

## 3 解题

### 3.1 查询每个人的总销售额

```mysql
select user.name, sum(sale_money)
from  user, sale
where user.id=sale.userid 
group by user.id;
```

### 3.2 查询每个人的总花费额

```mysql
select user.name, sum(sale_money)
from  user, sale
where user.id=sale.userid 
group by user.id;
```

### 3.3 把上面两个查询的结果作为表，进行关联查询

```mysql
select t1.name, 总销售额, 总花费额 from (
    select user.id as id, user.name as name, sum(sale_money) as 总销售额
    from  user, sale
    where user.id=sale.userid 
    group by user.id
) t1, (
    select user.id as id, user.name, sum(cost_money) as 总花费额
    from  user, cost
    where user.id=cost.userid 
    group by user.id
) t2
where t1.id = t2.id
```

