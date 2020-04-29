#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
import pymysql
config = {
        'user': 'root',
        'password': 'college',
        'host': 'db',
        'port': '3307',
        'database': 'employees'
    }

class DBase(object):
    def __init__ (self, host, db, port, user, password, **kwargs):
        self.host = host
        self.db = db
        self.port = port
        self.user = user
        self.password = password
        self.connection = self.get_connection()
        self.cursor = self.connection.cursor()

    def execute (self, query, args=None):
        if args is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, args)
        return self.cursor

    def executemany (self, query, args):
        self.cursor.executemany(query, args)

    def commit_and_close (self):
        if self.connection:
            self.connection.commit()
            self.connection.close()

    def rollback (self):
        if self.connection:
            self.connection.rollback()

    def autocommit (self, enable=True):
        if self.connection:
            self.connection.autocommit(enable)

    def commit (self):
        self.connection.commit()

    def rollback (self):
        self.connection.rollback()

    def close (self):
        if self.connection:
            self.connection.close()

    def __del__ (self):
        self.close()

    def __enter__ (self):
        return self

    def __exit__ (self, type, value, traceback):
        self.close()



class MySQLDBase(DBase):
    """MYSQL Database"""

    def execute_with_retry (self, func, *args, **kwargs):
        attempts = 0
        error = None
        while attempts < 3:
            try:
                func(*args, **kwargs)
                break
            except pymysql.Error, e:
                attempts += 1
                error = e
        if attempts < 3:
            return self.cursor
        else:
            raise error

    def safe_execute (self, query, args=None):
        return self.execute_with_retry(self.cursor.execute, query, args)

    def safe_execute_many (self, query, args):
        return self.execute_with_retry(self.cursor.executemany, query, args)

    def get_connection (self):
        connection = pymysql.connect(host=self.host, db=self.db, user=self.user, password=self.password)#, use_unicode=True)
        return connection


class Employees(MySQLDBase):
    def __init__(self):
        MySQLDBase.__init__(self, host='127.0.0.1',port=3007, db='employees', user='root', password='college')
