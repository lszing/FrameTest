from util.util_db import DbManager


# from util.util_db import DbManager_new


class db_Frame_Config:
    def get_sqlClient(self, db_conf: dict):
        # with DbManager_new(db_conf) as db:
        #     return db.selectOne
        return DbManager(db_conf).selectOne
