# 导入selenium 包
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from utils.path import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 创建一个 Chromdriver 的实例。Chrome()会从环境变量中寻找浏览器驱动
# driver = webdriver.Chrome(ChromeDriverManager(path=driver_path).install())
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(path=driver_path).install()))
# 打开网址
driver.get("https://ceshiren.com/")
WebDriverWait(driver,timeout=10).until(EC.visibility_of_element_located((By.ID,'123')))
# 关闭driver

driver.quit()