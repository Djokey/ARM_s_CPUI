import sqlite3


class ARMDataBase:
    def __init__(self, db='arm_db.db'):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def query(self, _sql):
        self.cursor.execute(_sql)
        self.conn.commit()
        _query = self.cursor.fetchall()
        self.conn.close()
        return _query


# If this py.file is main
if __name__ == "__main__":
    arm_db = ARMDataBase('arm_db.db')
    _sql = "SELECT * FROM headers"
    print(arm_db.query(_sql))

