import json
import os
from log.logpro import log

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ReadJson():
    def __init__(self, file_, filter=None):
        log.info(f'filter is  {filter} ')
        self.file_ = file_
        self.filter = filter

    def readJson(self):
        result = []
        if self.file_ is not None:
            try:
                self.case_data = path + '/data/' + self.file_ + '.json'
            except:
                log.fatal(f'{self.file_}.json is not isset in data/')
                raise FileNotFoundError
            with open(self.case_data, 'r', encoding='utf-8') as f:
                jsonData = json.load(f)
            # 1 filter=case1  path  指定文件指定case
            if self.filter is not None and self.filter != 'default':
                result.append(jsonData[self.filter])
            # 2 filter=all  path不传 执行全部case
            else:
                for key in jsonData:
                    result.append(jsonData[key])
        # 3 filter不传(default) path 指定文件全部case
        else:
            return self.get_all_data_file()
        return result

        # 获取data下全部文件加入列表批量执行

    def get_all_data_file(self):
        data_path = path + '/data/'
        for root, dirs, files in os.walk(data_path):
            file_list = files
        all_file_data = []
        for i in file_list:
            with open(data_path + i, 'r', encoding='UTF-8') as f:
                data = json.load(f)
                for key in data:
                    all_file_data.append(data[key])
        return all_file_data


if __name__ == '__main__':
    # print(ReadJson().readJson()[0])
    print(os.path.abspath(__file__))
