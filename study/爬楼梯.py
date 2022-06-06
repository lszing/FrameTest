'''
n层楼梯 每次只能走1阶或2阶 求有多少种方法
'''
import functools


# 我们用 f(x)f(x) 表示爬到第 xx 级台阶的方案数，考虑最后一步可能跨了一级台阶，也可能跨了两级台阶，所以我们可以列出如下式子：
# f(x) = f(x - 1) + f(x - 2)
# 它意味着爬到第 xx 级台阶的方案数是爬到第 x - 1 级台阶的方案数和爬到第 x - 2 级台阶的方案数的和

def climbStairs(n: int) -> int:
    n1, n2, r = 0, 0, 1
    for i in range(n):
        n1 = n2
        n2 = r
        r = n1 + n2
    return r


@functools.lru_cache(100)
def climbStairs1(n: int) -> int:
    return climbStairs1(n - 1) + climbStairs1(n - 2) if n > 2 else n


print(climbStairs(10))
print(climbStairs1(10))
