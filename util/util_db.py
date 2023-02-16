import pymysql

from log.logpro import log


class DbManager:
    conn = None
    cursor = None

    def __init__(self, db_conf):
        # if self.conn is None:
            # self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='testdb')
        try:
            self.conn = pymysql.connect(host=db_conf['HOST'], port=db_conf['PORT'], user=db_conf['USER'],
                                        password=db_conf['PASSWORD'])
        except:
            raise Exception('MySQL connect failed')
        if self.cursor is None:
            self.getCursor()

    def getCursor(self):
        self.cursor = self.conn.cursor()

    def getDbConn(self):
        return self.conn

    def selectAll(self, sql):
        self.cursor.execute(sql)
        ret = self.cursor.fetchall()
        return ret

    def selectOne(self, sql):
        self.cursor.execute(sql)
        ret = self.cursor.fetchone()
        return ret

    def exeCommit(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except pymysql.Error as e:
            self.conn.rollback()
            print(f'MySQL execute failed,ERROR {e.args[0]}:{e.args[1]}')

    '''
    tablename :表名
    attr_dict :属性键值对
    constraint :主外键约束
    '''

    def createTable(self, tablename, attr_dict, constraint):
        sql = ''
        sql_mid = ''
        for attr, value in attr_dict.items():
            sql_mid += '`' + attr + '`' + ' ' + value + ','
        sql += f'CREATE TABLE IF NOT EXISTS {tablename} ('
        sql += sql_mid
        sql += constraint
        sql += ') ENGINE=InnoDB DEFAULT CHARSET=uft8'
        print('createTable:' + sql)
        self.exeCommit(sql)

    # 开始事务
    def beginTransaction(self):
        self.conn.begin()

    def endTransaction(self, option):
        if option == 'commit':
            self.conn.commit()
        else:
            self.conn.rollback()

    def dispose(self, isEnd=1):
        if isEnd == 1:
            self.endTransaction('commit')
        else:
            self.endTransaction('rollback')
        self.cursor.close()
        self.conn.close()

    def test(self):
        sqlconn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='testdb')
        # 获取数据库游标
        cursor = sqlconn.cursor()
        sql = 'show databases'
        print(cursor.execute(sql))
        print(cursor.fetchall())
        cursor.close()
        sqlconn.close()


if __name__ == '__main__':
    DbManager().test()
    DbManager().selectAll()
