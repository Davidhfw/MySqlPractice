# Mysql实现Rank排名函数的方法汇总

## 问题描述

编写一个 SQL 查询来实现分数排名。如果两个分数相同，则两个分数排名（Rank）相同。请注意，平分后的下一个名次应该是下一个连续的整数值。换句话说，名次之间不应该有“间隔”。

## 解题思路

### 解题思路1

1. 采用表连接的方法，左表与又表进行比较，若左表数据小于右表，则对又表计数。
2. 按照左表ｉｄ分组。
3. 按照左表分数倒序排序。

#### 创建一个Grades表。

sql语句如下：

```mysql
CREATE TABLE `Grades` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL, 
    `grade` INT(2) NOT NULL, 
    PRIMARY KEY(`id`)
) ENGINE=InnoDB;
```

插入数据：

```mysql
INSERT INTO Grades VALUES (1, '张飞', 99);
INSERT INTO Grades VALUES (2, '关羽', 90);
INSERT INTO Grades VALUES (3, '刘备', 96);
INSERT INTO Grades VALUES (4, '诸葛亮', 99);
INSERT INTO Grades VALUES (5, '姜维', 88);
INSERT INTO Grades VALUES (6, '赵云', 78);
INSERT INTO Grades VALUES (7, '吕布', 75);
INSERT INTO Grades VALUES (8, '张辽', 88);
INSERT INTO Grades VALUES (9, '周瑜', 99);
INSERT INTO Grades VALUES (10, '曹操', 88);
```

这里区分下，在mysql8.0以上的版本，已经实现了ROW_NUMBER(), RANK()和 DENSE_RANK()函数， 具体用法可参考官方文档https://dev.mysql.com/doc/refman/8.0/en/window-function-descriptions.html#function_rank

我的mysql版本为8.0版本，分别使用上述三个函数，结果展示如下：

```mysql
mysql> SELECT grade, ROW_NUMBER() OVER w as 'row_number', RANK() OVER w as 'rank' ,  DENSE_RANK() OVER  w AS 'dense_rank'  FROM Grades  WINDOW w AS(ORDER BY grade);
+-------+------------+------+------------+
| grade | row_number | rank | dense_rank |
+-------+------------+------+------------+
|    75 |          1 |    1 |          1 |
|    78 |          2 |    2 |          2 |
|    88 |          3 |    3 |          3 |
|    88 |          4 |    3 |          3 |
|    88 |          5 |    3 |          3 |
|    90 |          6 |    6 |          4 |
|    96 |          7 |    7 |          5 |
|    99 |          8 |    8 |          6 |
|    99 |          9 |    8 |          6 |
|    99 |         10 |    8 |          6 |
+-------+------------+------+------------+
10 rows in set (0.00 sec)
```

如果mysql版本为5.6/5.7或以下，需要自己实现rank函数，这里我参考了网上其他人的代码，由于没有mysql5.6或者5.7的版本，因此代码的可用性无法验证，这里主要是以leetcode上的178为例。

建表语句如下

```mysql
mysql> CREATE  TABLE `Scores` 
(     
    `Id` INT(2)  AUTO_INCREMENT NOT NULL,     
    `Score` FLOAT(4)    NOT NULL ,      
    PRIMARY KEY(`Id`) 
) ENGINE=innodb;

```

插入数值

```mysql
INSERT INTO Scores VALUES(1, 3.50), (2, 3.65), (3, 4.00), (4, 3.85), (5, 4.00), (6, 3.65);
```

解题思路1 对应的代码

```mysql
SELECT s1.score, (SELECT COUNT(*) + 1 FROM (SELECT DISTINCT score From Scores) s2
WHERE s2.score >s1.score) as Rank from Scores s1 order by Rank;
```

2 使用变量来解决

```mysql
SELECT Score,
    cast((CASE
    WHEN @prev = Score THEN @cur
    WHEN @prev := Score THEN @cur := @cur + 1
    WHEN Score <= 0 THEN @cur := @cur + 1
    END) as signed) AS Rank
FROM Scores,
(SELECT @cur := 0, @prev := null) r
ORDER BY 
    Score DESC;
```

关于mysql变量的学习，大家可参考这篇CSDN博客https://blog.csdn.net/justry_deng/article/details/80597916?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task