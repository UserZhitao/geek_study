import allure
import pytest
from allure_commons.types import AttachmentType
import subprocess
import os
from utils.path import *
from selenium import webdriver
from test_game_second.loadUtils import LoadUtils
from utils.screenshot import *


@pytest.fixture
def get_hero_volume_limit():
    volume_limit = LoadUtils.load_yaml(test_data_path+"/hero.yaml")['volumeLimit']
    return volume_limit

boundary_value = LoadUtils.load_yaml(test_data_path+"/boundary_value.yaml")['boundary value']
@pytest.fixture(params=list(boundary_value['hero_name'].items()), ids=lambda item: f"{item[0]}")
# @pytest.fixture
def get_hero_name(request):
    print(request.param)
    return request.param

@pytest.fixture(params=list(boundary_value['hero_volume'].items()), ids=lambda item: f"{item[0]}")
# @pytest.fixture
def get_hero_volume(request):
    # request.param
    request.param = list(request.param)
    request.param[0] = request.param[0] + 1
    print(request.param)
    return request.param

@pytest.fixture
# @pytest.fixture(params=LoadUtils.load_yaml("test_data/equivalence_class.yaml")['invalid equivalence class'],ids=lambda params: f"{params[0]}-{params[1]}-{params[2]}")
# @pytest.fixture(params=LoadUtils.load_yaml("test_data/test.yaml")['data'])
def get_equivalence_class_value(request):
    if type(request.param[1]) == int:
        request.param[1] = request.param[1] + 1
    return request.param

# 在测试用例失败时进行截图的钩子函数
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # 如果测试用例失败且有driver对象
    if rep.when == "call" and rep.failed:

        # 将截图的路径添加到测试报告中
        allure.attach(screen_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)

# @pytest.fixture(scope="module",autouse=True)
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()




def test(get_equivalence_class_value):
    print(get_equivalence_class_value)