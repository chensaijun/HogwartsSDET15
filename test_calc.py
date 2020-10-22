#!/usr/bin/env python3
# -*- coding:utf -8 -*-
import pytest
from pythoncode.calculator import Calculator


class TestCALC:

    def setup_class(self):
        self.calc = Calculator()
        print("计算开始")

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a, b, expect', [
        [1, 2, 3], [100, 100, 200], [-1, -1, -2]
    ], ids=['case1', 'case2', 'case3'])
    def test_add(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a, b, expect', [
        [0.1, 0.1, 0.2], [0.1, 0.2, 0.3]
    ])
    def test_add_float(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    # def test_add1(self):
    #     #calc = Calculator()
    #     test_data = [
    #         [1, 2, 3], [4, 5, 9], [100, 100, 200]
    #     ]
    #     for i in range(0, len(test_data)):
    #         result1 = self.calc.add(test_data[i][0], test_data[i][1])
    #         assert result1 == test_data[i][2]
    #
    # def test_add2(self):
    #     #calc = Calculator()
    #     result = self.calc.add(400, 50)
    #     assert result == 450

    @pytest.mark.parametrize('a,b,expect', [
        [2, 1, 1], [100, 0, 100], [0, '-100', -100]
    ])
    def test_sub(self, a, b, expect):
        # calc1 = Calculator()
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [
        [2, 2, 4], [100, 100, 10000], [0, 10, 0], [5, 0, 0]
    ])
    def test_mul(self, a, b, expect):
        # calc2 = Calculator()
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize('a, b, expect', [
        [9, 3, 3], [-100, 10, -10], [1, 2, 0.5], [0, 9, 0]
    ])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect

    # @pytest.mark.parametrize('a, b',[
    #    [10,0],[-5,0]
    # ])
    def test_div_zero(self):
        try:
            result = self.calc.div(10, 0)
        except ZeroDivisionError as result:
            print("除数不能为0", result)
