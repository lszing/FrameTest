#输入一个正整数 这个正整数每位数字可以任意调换顺序 找到比这个正整数大的最小数
def selectMin(num):
    #如果输入数是个位 直接返回
    if num <= 9:
        return num
    #int转string切分加入列表中
    split = []
    for i in str(num):
        split.append(int(i))
    #排除654321这种情况 直接返回
    for i in range(len(split)):
        if split[i + 1] > split[i]:
            break
        elif i + 2 == len(split):
            return num
    # 倒叙遍历 从右到左找到第一位 右侧数大于当前数的位置
    for i in range(len(split) - 1, -1, -1):
        print(i)
        if split[i - 1] < split[i]:
            tmp = []
            # range(0,5) 返回 0,1,2,3,4
            for j in range(i, len(split)):
                tmp.append(split[j])
            # 给tmp排序 冒泡排序
            print("list need sort ",tmp)
            for k in range(len(tmp)):
                for g in range(len(tmp) - k - 1):
                    if tmp[g] > tmp[g + 1]:
                        tmp[g], tmp[g + 1] = tmp[g + 1], tmp[g]
            print("list sorted ", tmp)
            # 将分割位插入切分后列表第一位
            tmp.insert(0, split[i - 1])
            print("", tmp)
            for h in range(len(tmp)):
                if tmp[0] < tmp[h]:
                    tmp[0], tmp[h] = tmp[h], tmp[0]
                    break
            #切分原列表并拼接
            result = split[0:(i - 1)] + tmp
            #列表转字符串
            stt = ''
            for i in range(len(result)):
                stt += str(result[i])
            return int(stt)
        elif i - 1 == 0:
            return num


if __name__ == '__main__':
    print(selectMin(65321525123))
