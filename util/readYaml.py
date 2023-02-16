import os
import yaml


class ReadYaml:
    def readYaml(self, path):
        ralpath = os.path.dirname(os.path.dirname(__file__))
        yamlpath = ralpath + path
        print(yamlpath)
        with open(yamlpath, 'r', encoding='utf-8') as f:
            yamlData = yaml.load(f, Loader=yaml.FullLoader)
        return yamlData


if __name__ == '__main__':
    r = ReadYaml()
    yamlData = r.readYaml('/data/test.yaml')
    print(yamlData)
