import uuid

import identifier as identifier
import redis
import time

redis_conn_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, password='lsz', decode_responses=True)
redis_client = redis.Redis(redis_conn_pool)


# 获取一个分布式锁
def acquire_clock(lock_name, acquire_time=10, time_out=10):
    # 生成唯一id
    identifier = str(uuid.uuid4())
    # 客户端获取锁的结束时间
    end = time.time() + acquire_time
    # key
    lock_names = 'lock_name' + lock_name
    while time.time() < end:
        # 设置锁，并设置过期时间
        if redis_client.setex(lock_names, time_out, identifier):
            return identifier
        # 如果锁存在，且这个锁没有设置过期时间，则设置过期时间
        elif redis_client.ttl(lock_names) == -1:
            redis_client.expire(lock_names, time_out)
        time.sleep(0.001)
    # 若超过获取锁时间仍没获取到锁则放回False
    return False


# 释放锁
def release_lock(lock_name, identifier):
    lock_names = 'lock_name' + lock_name
    # python 中 redis 事务是通过pipeline的封装实现的
    with redis_client.pipeline() as pipe:
        while True:
            try:
                # 通过watch命令监听key,若该key未被其他客户端修改值时，事物执行成功。当事物运行时刚好锁过期被其他客户端更改了锁的值，则事物失败
                pipe.watch(lock_names)
                if pipe.get(lock_names) == identifier:
                    # multi命令用于开启第一事务，总是返回ok
                    # multi执行后，客户端可以继续向服务器发送任意多条命令，这些命令不会立即执行，而会被放到一个队列中，当EXEC命令被调用时，所有队列的命令才会被执行
                    pipe.multi()
                    # 删除key，释放锁
                    pipe.delete(lock_names)
                    # execute命令负责触发并执行事物中的所有命令
                    pipe.execute()
                    return True
                pipe.unwatch()
                break
            except redis.exceptions.WatchError:
                # 若释放锁期间，有其他
                pass
    return False


def acquire_lock1(lock_name, value, get_time=10, expire_time=10):
    end = time.time() + get_time
    lock_names = 'lock_name' + lock_name
    while time.time() < end:
        if redis_client.setex(lock_names, expire_time, value):
            return "get lock"
        elif redis_client.ttl(lock_names) == -1:
            redis_client.expire(lock_names, expire_time)
        time.sleep(0.001)
    return "lock failed"


def release_lock1(lock_name, value):
    lock_names = 'lock_name' + lock_name
    with redis_client.pipeline() as pipe:
        while True:
            try:
                pipe.watch(lock_names)
                if pipe.get(lock_names) == value:
                    pipe.multi()
                    pipe.delete(lock_names)
                    pipe.execute()
                    return 'delete lock success'
                pipe.unwatch()
                break
            except redis.WatchError:
                pass
    return 'delete lock failed'


def acquire_lock2(lock_name, value, acquire_time=10, expire_time=10):
    end = time.time() + acquire_time
    lock_names = 'lock_name' + lock_name
    while time.time() < end:
        if redis_client.setex(lock_names, expire_time, value):
            return 'lock success'
        elif redis_client.ttl(lock_names) == -1:
            redis_client.expire(lock_name, expire_time)
        time.sleep(0.001)
    return 'lock failed'


def release_lock2(lock_name, value):
    lock_names = 'lock_name' + lock_name
    with redis_client.pipeline() as pipe:
        while True:
            try:
                pipe.watch(lock_names)
                if pipe.get(lock_names)==value:
                    pipe.multi()
                    pipe.delete(lock_names)
                    pipe.execute()
                    return 'delete lock success'
                pipe.unwatch()
                break
            except redis.WatchError:
                pass
    return 'lock release failed'
