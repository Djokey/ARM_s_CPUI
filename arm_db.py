import sqlite3


class ARMDataBase:
    def __init__(self, db='arm_db.db'):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def query(self, _sql):
        self.cursor.execute(_sql)
        self.conn.commit()
        _query = self.cursor.fetchall()
        return _query

    def close(self):
        self.conn.close()


# If this py.file is main
if __name__ == "__main__":
    _db = ARMDataBase('arm_db.db')

    _sql = "SELECT id_prog FROM groups WHERE id_group=" + str('1')
    stud_group_prog_id = _db.query(_sql)

    _sql = "SELECT prog_name FROM programs WHERE id_prog=" + str(stud_group_prog_id[0][0])
    stud_group_prog_name = _db.query(_sql)

    print(stud_group_prog_name[0][0])

    _db.close()

