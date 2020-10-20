import pytest
from pythoncode.calculator import Calculator
import yaml


def read_yaml(key,indirect=False):
    with open('../testing/calc.yaml',encoding='utf-8') as f:
        data = yaml.safe_load(f)
        print(data)
        parms = data.get(key).get("parms")
        ids = data.get(key).get("ids")
        return [parms,indirect,ids]



@pytest.mark.usefixtures("start")
class TestCase():


    def setup_class(self):
        self.calc = Calculator()


    def teardown_class(self):
        pass

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expect",*read_yaml("add"))
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect",*read_yaml("sub"))
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expect",*read_yaml("mul"))
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,expect",*read_yaml("div"))
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect

