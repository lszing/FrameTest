import json
import os
from log.logpro import log


class ReadJson():
    def __init__(self, file_ ,filter=None):
        log.info(f'filter is  {filter} ')
        self.file_ = file_
        self.filter = filter
        dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        try:
            self.case_data = dir + '\\data\\' + self.file_+'.json'
        except:
            log.warning(f'{self.file_}.json is not isset')
            #todo 改成更好的处理逻辑
            assert 1==2
        log.info(f'Start executing data source is {self.case_data}')

    def readJson(self):
        classname = self.__class__.__name__
        # print('classname=======',classname)
        # ralpath=os.path.dirname(os.path.dirname(__file__))
        # yamlpath=ralpath+path
        # print(yamlpath)
        result = []
        with open(self.case_data, 'r', encoding='utf-8') as f:
            jsonData = json.load(f)
        # 将字典按照key（case1.2.3.4....）切分并插入列表中
        #判断入参
        if self.filter is not None and self.filter != 'default':
            result.append(jsonData[self.filter])
        else:
            for key in jsonData:
                # result.append({key: jsonData[key]})
                result.append(jsonData[key])

        # result.append(jsonData)
        #返回列表
        return result
        # todo  暂时返回json
        # return jsonData


if __name__ == '__main__':
    # print(ReadJson().readJson()[0])
    print(os.path.abspath(__file__))