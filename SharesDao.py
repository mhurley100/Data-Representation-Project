import mysql.connector
from mysql.connector import cursor
import dbconfig as cfg

class ShareDao:
    db = ""
    def __init__(self):
            self.db = mysql.connector.connect(
            host =      cfg.mysql['host'],
            user=       cfg.mysql['user'],
            password =  cfg.mysql['password'],
            database  = cfg.mysql['database']
        )
        #print ("connection made")

    def create(self, share):
        cursor = self.db.cursor()
        sql = "insert into shares (id, symbol, name, price) values (%s,%s,%s,%s)"
        values = [
            share['id'],
            share['symbol'],
            share['name'],
            share['price']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from shares'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, id):
        cursor = self.db.cursor()
        sql = 'select * from shares where id = %s'
        values = [ id ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, share):
       cursor = self.db.cursor()
       sql = "update shares set symbol = %s, name = %s, price = %s where id = %s"
       values = [
           share['symbol'],
           share['name'],
           share['price'],
           share['id']

       ]
       cursor.execute(sql, values)
       self.db.commit()
       return share

    def delete(self, id):
       cursor = self.db.cursor()
       sql = 'delete from shares where id = %s'
       values = [id]
       cursor.execute(sql, values)
       
       return {}



    def convertToDict(self, result):
        colnames = ['id','symbol', 'name', 'price']
        share = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                share[colName] = value
        return share

shareDao = ShareDao()