import redis


class redisManager:
    redis_util_map = {
        'string': '',
        'map': '',
        'set': '',
        'zset': '',
        'list': '',

    }

    def __init__(self, redis_conf):
        self.redis_conn_pool = redis.ConnectionPool(host=redis_conf['host'], port=redis_conf['port'],
                                                    db=redis_conf['db'],
                                                    password=redis_conf['password'],
                                                    decode_responses=True)
        self.r = redis.Redis(connection_pool=self.redis_conn_pool)
        # self.host = kwargs['host']
        # self.port = kwargs['port']
        # self.db = kwargs['db']
        # self.password = kwargs['password']

    def get_string(self, key):
        return self.r.get(key)

    def set_key(self, key, value, expire_time):
        return self.r.setex(key, expire_time, value)

    def del_key(self, key_name):
        return self.r.delete(key_name)

    def get_key_expire(self, name):
        return self.r.ttl(name)

    def get_all_keys(self) -> list:
        return self.r.keys()

    def get_key_type(self, key):
        return self.r.type(key)

    def get_list(self, key, start=0, end=-1):
        return self.r.lrange(key, start, end)

    def get_set(self, key):
        return self.r.smembers(key)

    def get_map(self, hash_key: str):
        num = len(hash_key.split('.'))
        if num > 1:
            raise Exception(f'key [{hash_key}] error,length>2')
        # 两个搜索指定key
        if num == 2:
            return self.r.hget(hash_key[0], hash_key[1])
        # 一个字符串搜索该key下所有hash
        elif num == 1:
            return self.r.hgetall(hash_key)


# r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0, password='lsz', decode_responses=True)
# r.set('test', 'test')
# print(type(r.get('test')))

redis_conn_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, password='lsz', decode_responses=True)
r = redis.Redis(connection_pool=redis_conn_pool)
print(r.get('test'))
# ex过期时间

r.set('a', '1', ex=200)
r.setex('b', 2000, '2')
print(r.keys())
