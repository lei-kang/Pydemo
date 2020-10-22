import pytest

# 分组名称，可一在终端指定名字运行用例
@pytest.mark.login
def test_login1():
    print("登录用例")


@pytest.mark.login
def test_login2():
    print("登录用例2")


@pytest.mark.search
def test_search1():
    print("搜索用例")


@pytest.mark.search
def test_search2():
    print("搜索用例")
