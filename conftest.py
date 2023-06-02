import pytest
from allure_commons.types import AttachmentType
import subprocess
import os
from utils.path import *
@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    generate_allure_report()

def generate_allure_report():
    # 执行 Allure 命令生成报告
    subprocess.call(["allure", "generate", report_path + '/allure-xml', "-o", report_path + '/allure-report', "--clean"])
    # subprocess.call(["allure", "open", 'report/allure-report'])
