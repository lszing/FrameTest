# 文本文档  每行一个字符串  有可能是重复的  统计每个字符串重复次数
import os


def solution(path):
    dict = {}
    with open(path, 'r', encoding='UTF-8') as f:
        # netstat -tunlp|grep port
        # ll /proc/i
        # cat  1.txt| sort uniq wc -l
        line = f.readlines()
        for i in line:
            i = i[:len(i) - 1]
            if i in dict.keys():
                dict[i] += 1
            else:
                dict[i] = 1

    return dict


# 班级  姓名 分数
# select 班级,count(*) from table group by 班级 having 分数<60

if __name__ == '__main__':
    # 字符串前面+u  则后面字符串以Unicode格式进行编码 一般用在中文字符串前面 防止因为源码储存格式问题，导致出现乱码
    # 字符串前面+r  去掉反斜杠的转义机制  即\为字符串
    # 字符串前面+b  则后面字符串是bytes类型
    path = u'C:/Users/v_lushuzhi_dxm/Desktop/demo_testPro/demo_testPro/test.txt'
    print(solution(path))
