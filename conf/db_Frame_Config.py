from util.util_db import DbManager


class db_Frame_Config:
    def get_sqlClient(self, db_conf: dict):
        return DbManager(db_conf).selectOne
