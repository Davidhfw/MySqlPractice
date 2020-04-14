# 初始化数据库连接
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float, INT, FLOAT, VARCHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class TestDb:
    def __init__(self):
        self.engine = create_engine('mysql+mysqlconnector://root:hfw610321@localhost:3306/whf_test')
        self.db_session = sessionmaker(bind=self.engine)
        # 创建session对象
        self.session = self.db_session()

    def update(self, target_class, query_filter, target_obj):
        """
        更新操作通用方法
        :param target_class: 表对象
        :param query_filter: 查询条件
        :param target_obj: 更新目标对象
        :return:
        """
        try:
            self.session.query(target_class).filter(query_filter).update()
# 初始化数据库连接， 修改为你的数据库用户名和密码
engine = create_engine('mysql+mysqlconnector://root:hfw610321@localhost:3306/whf_test')


# 定义Player对象
class Player(Base):
    # 表的名字
    __tablename__ = 'player'

    # 表的结构
    player_id = Column(Integer, primary_key=True, autoincrement=True)
    team_id = Column(Integer)
    player_name = Column(String(255))
    height = Column(Float(3, 2))


# 创建DBSession类型
DBSession = sessionmaker(bind=engine)
# 创建session对象
session = DBSession()

# 创建Player对象
new_player = Player(team_id=1003, player_name="约翰-科斯", height=2.08)
# 添加到session
session.add(new_player)
# 提交即保存到数据库
session.commit()
# 关闭session
session.close()

# 增加to_dict()方法到Base类中
