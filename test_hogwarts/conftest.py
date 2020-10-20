from typing import List

import pytest


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
