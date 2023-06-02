import yaml
from utils.path import *
class LoadUtils(object):

    @classmethod
    def load_yaml(cls,yaml_file):
        data = yaml.safe_load(open(yaml_file, encoding='utf-8'))
        return data

if __name__ == '__main__':
    # 不使用类方法的方式
    # load_utils = LoadUtils()
    # load_utils.load_yaml()
    # 使用类方法调用
    print(LoadUtils.load_yaml(test_data_path + "/boundary_value.yaml")['boundary value'])