# 获取文件流
import os

import yaml

from config import base_url


def read_yaml(filename):
    with open(base_url+os.sep+"data"+os.sep+filename, "r", encoding="utf-8") as f:
        url_list = []
        for data in yaml.safe_load(f).values():
            url_list.append(tuple(data.values()))
            return url_list



if __name__ == '__main__':
    print(read_yaml("login.yaml"))