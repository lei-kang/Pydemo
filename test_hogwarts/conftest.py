from typing import List

import pytest
import yaml

@pytest.fixture(scope="module")
def start():
    print("开始计算")
    yield
    print("计算结束")


def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts-FIS")  # group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',  # 默认值
                      dest='env',  # 存储的变量
                      help='set your run env'  # 参数说明
                      )


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')

    if myenv == 'test':
        datapath = "datas/env/data.yml"
    elif myenv == 'dev':
        datapath = "datas/dev/data.yml"

    with open(datapath,encoding='utf-8') as f:
        datas = yaml.safe_load(f)

    print(datas)

    return myenv, datas
