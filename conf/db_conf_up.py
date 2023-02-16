from conf.db_Frame_Config import db_Frame_Config


class DbConf(db_Frame_Config):
    test_db = {
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'root',
        'CHARSET': '',
        'CONNECT_TIMEOUT': ''
    }


if __name__ == '__main__':
    sql_client = DbConf().get_sqlClient(DbConf.paylater_test_db)
    reuslt=sql_client('select * from *** where user_pin=\'lushuzhi\'')
    print(reuslt)