from functools import lru_cache


def sort(nums):
    a = lambda n: (nums.count(n), -n)
    print(a(1))
    print(a(4))
    print(a(3))
    #lru_cache 缓存装饰器  lru_cache(None)最多缓存次数无限制
    print(sorted(nums, key=lru_cache(None)(lambda n: (nums.count(n), -n))  ))
    return sorted(nums, key=lambda n: (nums.count(n), -n))


print(sort([1, 1, 1, 4, 4, 3, 5]))
