# from unittest import TestCase
import pytest,allure
from allure import attachment_type
from game.hero_management import HeroManagement
from test_game_second.loadUtils import LoadUtils
from utils.path import *
from utils.screenshot import *
class TestHeroAdd():

    @classmethod
    def setup_class(cls):
        cls.hero_management = HeroManagement()

    @staticmethod
    def hero_name_data(test_type=None):
        name_data = list(LoadUtils.load_yaml(test_data_path+"/boundary_value.yaml")['boundary value']['hero_name'].items())
        return name_data

    @staticmethod
    def hero_volume_data(test_type=None):
        name_data = list(LoadUtils.load_yaml(test_data_path+"/boundary_value.yaml")['boundary value']['hero_volume'].items())
        return name_data

    @staticmethod
    def hero_equivalence_class_value(test_type=None):
        name_data = LoadUtils.load_yaml(test_data_path+"/equivalence_class.yaml")[test_type]
        return name_data


        # 增加英雄测试用例
    @allure.step('test boundaryValue for create hero')
    @pytest.mark.boundaryValue
    @pytest.mark.order(0)
    @pytest.mark.parametrize("hero_power", [20,5000])
    def test_create_hero(self, get_hero_name, get_hero_volume,get_hero_volume_limit,hero_power):
        hero_name = get_hero_name[0]
        hero_volume = get_hero_volume[0]
        res = self.hero_management.create_hero(hero_name=hero_name, hero_volume=hero_volume, hero_power=hero_power,get_hero_volume_limit=get_hero_volume_limit)
        expected_result = (get_hero_name[1] and get_hero_volume[1])
        assert res == expected_result

    @allure.step('test effectiveEquivalenceClass for create hero')
    @pytest.mark.effectiveEquivalenceClass
    # @pytest.mark.parametrize('get_hero_name',hero_name_data('Reasonable boundary value'),indirect=True,ids=lambda item: f"{item[0]}")
    @pytest.mark.parametrize('get_equivalence_class_value',hero_equivalence_class_value('effective equivalence class'),indirect=True,ids=lambda params: f"{params[0]}-{params[1]}-{params[2]}")
    def test_create_hero_success(self,get_equivalence_class_value,get_hero_volume_limit):
        hero_name = get_equivalence_class_value[0]
        hero_volume = get_equivalence_class_value[1]
        hero_power = get_equivalence_class_value[2]
        res = self.hero_management.create_hero(hero_name=hero_name, hero_volume=hero_volume, hero_power=hero_power,
                                               get_hero_volume_limit=get_hero_volume_limit)
        expected_result = True
        # allure.attach(screen_as_png(),"screenshot",attachment_type=attachment_type.PNG)
        assert res == expected_result

    @pytest.mark.invalidEquivalenceClass
    @pytest.mark.order(1)
    @pytest.mark.parametrize('get_equivalence_class_value',hero_equivalence_class_value('invalid equivalence class'),indirect=True,ids=lambda params: f"{params[0]}-{params[1]}-{params[2]}")
    def test_create_hero_failed(self, get_equivalence_class_value,get_hero_volume_limit):
        hero_name = get_equivalence_class_value[0]
        hero_volume = get_equivalence_class_value[1]
        hero_power = get_equivalence_class_value[2]
        res = self.hero_management.create_hero(hero_name=hero_name, hero_volume=hero_volume, hero_power=hero_power,
                                               get_hero_volume_limit=get_hero_volume_limit)
        assert res == False




