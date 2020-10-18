import pytest

def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5



@pytest.mark.parametrize('a,n', [[1, 2,],[1,3]])
@pytest.mark.parametrize('b,c', [[1, 2,],[1,3]])
def test_parm(a,n,b,c):
    print(a, n)


@pytest.mark.parametrize("a,b", [(2, 1),(1, 2)])
@pytest.mark.parametrize("m,n", [(1, 6), (2, 3)])
def test_case(a, b,m,n):
    print(a+b)
    print("我是测试函数test_fixture_param_and_parametrize，参数a是%s，b是%s" % (a, b))
    # print("我fixture_param现在是：%s"%fixture_param)

