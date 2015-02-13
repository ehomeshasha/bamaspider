# -*- coding: utf-8 -*-


import MySQLdb


class MysqlClient():

    conn = None
    cursor = None

    def __init__(self, **kwargs):
        if self.conn == None:
            self.conn = MySQLdb.connect(host=kwargs['host'],
                                        port=kwargs['port'],
                                        user=kwargs['user'],
                                        passwd=kwargs['passwd'],
                                        db=kwargs['db'],
                                        charset=kwargs['charset'])


    def fetchAll(self, query):
        if self.cursor == None:
            self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        return self.cursor.fetchall()



    def query(self, query):
        if self.cursor == None:
            self.cursor = self.conn.cursor()
        #print query
        res = self.cursor.execute(query)
        self.conn.commit()
        return res

    def close(self):
        if self.cursor != None:
            self.cursor.close()
        if self.conn != None:
            self.conn.close()