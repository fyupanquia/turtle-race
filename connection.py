import pymysql

class DataBase:
    
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='my-secret-pw',
            db='turtle_race'
        )

        self.cursor = self.connection.cursor()

        print("Connected successfully")

    def getLog(self):
        log = None
        sql = 'SELECT * FROM LOG ORDER BY ID DESC'
        try:
            self.cursor.execute(sql)
            log = self.cursor.fetchall()

            print("Got successfully")
        except Exception as err:
            print(f'Something wrong: {str(err)}')
            raise
        return log

    def saveLog(self, bet, winner):
        sql = "INSERT INTO LOG SET BET='{}', WINNER='{}', CREATED_AT=NOW()".format(bet, winner)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()

            print("Saved successfully")
        except Exception as err:
            print(f'Something wrong: {str(err)}')
            raise