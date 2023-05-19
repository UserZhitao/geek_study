import pytest
import sys,os
import subprocess
def run_tests():
    current_path = os.path.abspath(__file__)
    directory_path = os.path.dirname(current_path)
    # base_path = os.path.split(directory_path)[0]
    print(directory_path)
    report_path = os.path.abspath(os.path.join(directory_path,'report')) + '/allure-xml'
    print(report_path)

    args = ["-s",
            "--alluredir", report_path, "--clean-alluredir"
            ]

    # 执行 Pytest
    pytest.main(args)

    # subprocess.call(["allure", "generate", report_path, "-o", report_path, "--clean"])

if __name__ == "__main__":
    sys.exit(run_tests())