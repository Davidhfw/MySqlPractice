# mysql笔试题汇总

## 1 业务培训信息管理

S(S#, SN, SD, SA)  // S#, SN, SD, SA分别代表学号，学员姓名，所属单位和学员年龄  
C(C#, CN)  // C#, CN分别代表课程编号和课程名称  
SC(S#, C#, G)  // S#, C#, G分别代表学号，所选课程编号和学习成绩  

 (1) 使用标准sql嵌套查询语句查询课程名称为‘税收基础’的学员学号和姓名

```mysql
SELECT S#, SN FROM S WHERE S# IN (SELECT S# FROM C, SC WHERE C.C#=SC.C# AND CN = '税收基础')
```

(2) 使用标准SQL嵌套语句查询选修课程编号为'C2'的学员的学员姓名和所属单位

```mysql
SELECT SN, SD FROM S, SC WHERE S.S# = SC.S# AND SC.C# = 'C2'
```

(3)使用标准sql嵌套语句查询不选修课程编号为‘C5’的学员姓名和所属单位

```mysql
SELECT SN, SD FROM S WHERE S# NOT IN (SELECT S# FROM SC WHERE C# = 'C5')
```

(4) 查询选修课程的人数

```mysql
SELECT 学员人数=COUNT(DISTINCT S#) FROM SC
```

(5)查询选修课程超过5门的学员学号和所属单位

```mysql
SELECT SN, SD FROM S WHERE S# IN (SELECT S# FROM SC GROUP BY S# HAVING COUNT(DISTINCT C#) >5)
```

## 2 查询A(ID, Name)表中第31至40条记录，ID作为主键可能不是连续增长的序列

```mysql
SELECT TOP 10 * FROM A WHERE ID > (SELECT MAX(ID) FROM (SELECT TOP 30 ID FROM A ORDER BY A) T) order by A
```

## 3 数据库设计题

学生表的表结构如下：

Student学生表（学号，姓名， 性别， 年龄， 组织部门）  

Course课程表（编号，课程名称）

Sc选课表（学号， 课程编号和成绩）

1 写一个sql语句，查询选修了‘计算机原理’的学生学号和姓名

```mysql
SELECT 学号, 姓名 FROM Student WHERE 学号 IN (SELECT 学号 FROM Course, Sc WHERE Sc.学号 = Course.学号 AND Course.课程名称 = '计算机原理')
```

2 写一个sql语句，查询‘周星驰’同学选修了的课程名称

```mysql
SELECT cname FROM Course WHERE cno IN (SELECT cno FROM Sc WHERE sno = (SELECT sno From Student where sname='周星驰'))
```

3 写一个sql语句，查询选修了5门课程的学生学号和姓名

```mysql
SELECT sno, sname FROM Student WHERE sno in (Select sno from sc group by sno having count(sno) =5)
```

