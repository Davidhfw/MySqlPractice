# -×- coding：utf8 -*-

import mysql.connector
import traceback
# 打开数据库链接
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='hfw610321',
    database='whf_test',
    auth_plugin='mysql_native_password'
)
# 获取操作游标
cursor = db.cursor()
# 执行SQL语句
# cursor.execute('SELECT VERSION()')
# sql = 'INSERT INTO player (team_id, player_name, height) VALUES(%s, %s, %s)'
# val = (1003, "约翰-柯林斯", 2.08)
# cursor.execute(sql, val)
# print(cursor.rowcount, "记录插入成功。")
# sql1 = 'SELECT player_id, player_name, height FROM player WHERE height >= 2.08'
# cursor.execute(sql1)
# data = cursor.fetchall()
# for each_player in data:
#     print(each_player)
# sql = 'UPDATE player SET height = %s WHERE player_name = %s'
# val = (2.09, "约翰-柯林斯")
# cursor.execute(sql, val)
# db.commit()
# print(cursor.rowcount, '记录被修改。')
# 获取一条数据
# data = cursor.fetchone()
# print('MYSQL版本： %s' % data)
# # 关闭游标&数据库连接
try:
    sql = 'INSERT INTO player (team_id, player_name, height) VALUES (%s, %s, %s)'
    val = (1003, "约翰-柯斯", 2.08)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "记录插入成功。")
except Exception as e:
    traceback.print_exc()
    db.rollback()
finally:
    cursor.close()
    db.close()
