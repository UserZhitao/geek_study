import pytest
from allure_commons.types import AttachmentType
import subprocess
import os

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    generate_allure_report()

def generate_allure_report():
    current_path = os.path.abspath(__file__)
    directory_path = os.path.dirname(current_path)
    print(directory_path)
    report_path = os.path.abspath(os.path.join(directory_path, 'report')) + '/allure-xml'
    # 执行 Allure 命令生成报告
    subprocess.call(["allure", "generate", report_path, "-o", 'report/allure-report', "--clean"])
    # subprocess.call(["allure", "open", 'report/allure-report'])
