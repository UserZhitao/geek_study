# from unittest import TestCase
import pytest
from game.hero_management import HeroManagement

class TestHeroManagement():

    @classmethod
    def setup_class(cls):
        cls.hero_management = HeroManagement()

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    @classmethod
    def teardown_class(cls):
        pass

        # 增加英雄测试用例
    @pytest.mark.order(0)
    @pytest.mark.parametrize("hero_name, hero_volume, hero_power, expected_result", [
        ("zhangsan", 1, 30, True),  #name 有效， volume在合理范围内， power 正整数
        ("lisi", 2, 20, True),
        ("wangwu", 98, 10, True),
        ("zhaoliu", 99, 10, True),
        ("sunqi", 50, 5000, True)
    ],ids=lambda params: f"{params}")
    def test_create_hero_success(self, hero_name, hero_volume, hero_power, expected_result):
        res = self.hero_management.create_hero(hero_name=hero_name, hero_volume=hero_volume, hero_power=hero_power)
        assert res == expected_result

    @pytest.mark.order(1)
    @pytest.mark.parametrize("hero_name, hero_volume, hero_power, expected_result", [
        (1, 1, 30, False), #name is number
        (False, 1, 30, False), #name is bool
        ("test01", 'abc', 20, False), #volume is string
        ("test01", True, 10, False), #valume is bool
        ("test01", 0, 10, False), #volume is 0
        ("test01", 100, 5000, False), #volume is 100
        ("test01", 45, 0, False),  #power is 0
        ("test01", 0, -1, False),  #power < 0
        ("test01", 0, 'abc', False), #power is str
        ("test01", 0, True, False), #power is bool
        ("test01", 0, 10.00, False),#power is float
    ],ids=lambda params: f"{params}")
    def test_create_hero_failed(self, hero_name, hero_volume, hero_power, expected_result):
        res = self.hero_management.create_hero(hero_name=hero_name, hero_volume=hero_volume, hero_power=hero_power)
        assert res == expected_result

    @pytest.mark.parametrize("hero_name, hero_volume", [
        ("zhangsan", 1), #name 存在， volume 在合理范围内
        ("zhangsan", 2),
        ("zhangsan", 98),
        ("zhangsan", 99),
        ("zhangsan", 50)
    ], ids=lambda params: f"{params}")
    def test_update_hero_success(self, hero_name, hero_volume):
        res = self.hero_management.update_hero(hero_name, hero_volume)
        assert res['name'] == hero_name
        assert res['volume'] == hero_volume

    @pytest.mark.parametrize("hero_name, hero_volume, expected_result", [
        ('NotExisted', 1,  False),  # name is not existed
        (1, 1, False), #name is int == not existed
        (False, 1, False),  # name is bool == not existed
        ("lisi", 'abc',False),  # name is existed but volume is string
        ("lisi", True, False),  # name is existed but volume is bool
        ("lisi", 0, False),  # name is existed but volume is 0
        ("lisi", 100, False),  # name is existed but  volume is 100
    ], ids=lambda params: f"{params}")
    def test_update_hero_failed(self,hero_name,hero_volume,expected_result):
        res = self.hero_management.update_hero(hero_name, hero_volume)
        assert res == False

    @pytest.mark.parametrize("hero_name,expected_result", [
        ("zhangsan", {'name': 'zhangsan', 'power': 30, 'volume': 50}),
        ("lisi", {'name': 'lisi', 'power': 20, 'volume': 2}),
        ("NoExisted", False),
        (123, False),
        (True, False)
    ], ids=lambda params: f"{params}")
    def test_find_hero(self,hero_name,expected_result):
        res = self.hero_management.find_hero(hero_name)
        assert res == expected_result,"Find hero is failed"

    @pytest.mark.order(-1)
    @pytest.mark.parametrize("hero_name, expected_result", [
        ("zhaoliu",True),
        ("sunqi", True),
        ("NoExisted", False),
        (123, False),
        (True, False)
    ], ids=lambda params: f"{params}")
    def test_delete_hero(self, hero_name, expected_result):
        res = self.hero_management.delete_hero(hero_name)
        if expected_result:
            assert res,'delete hero failed'

        else:
            assert res == False,'the not existed hero is deleted!!!!'




