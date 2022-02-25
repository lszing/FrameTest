#coding:utf-8
import time



class Solution:
    def dayOfYear(self, date: str) -> str:
        # time.strptime(date, "%Y-%m-%d")返回以下内容 [-2]返回元组倒数第二个元素
        # time.struct_time(tm_year=2021, tm_mon=3, tm_mday=11, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=70, tm_isdst=-1)
        return time.strptime(date, "%Y-%m-%d")[-2]

    def dayOfyear1(self, date: str) -> int:
        a = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # map(function,iterable) eg:map(int,[1,2])-->int(1),int(2)
        y, m, d = map(int, date.split('-'))
        if y != 1900 and y % 4 == 0:
            a[2] += 1
        # sum(iterable)
        return sum(a[:m]) + d

    def dayOfyear2(self, date: str) -> int:
        isLeap = lambda y: y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)
        y, m, d = int(date[:4]), int(date[5:7]), int(date[8:])
        month = [31, 29 if isLeap(y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(month[:m - 1]) + d


if __name__ == '__main__':
    print(Solution().dayOfYear('2000-03-12'))
    print(Solution().dayOfyear1('2000-03-12'))
    print(Solution().dayOfyear2('2000-03-12'))