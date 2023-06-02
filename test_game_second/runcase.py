import pytest
import sys,os
from utils.path import *
import subprocess
def run_tests():
    new_add_hero_case_path = test_game_second_path + '/test_hero_add.py'
    allure_step_path = test_game_second_path+'/test_allure_step.py'
    args = ["-s",new_add_hero_case_path,
            "--alluredir", report_path+'/allure-xml', "--clean-alluredir"
            ]

    # 执行 Pytest
    pytest.main(args)

    # subprocess.call(["allure", "generate", report_path, "-o", report_path, "--clean"])

if __name__ == "__main__":
    sys.exit(run_tests())