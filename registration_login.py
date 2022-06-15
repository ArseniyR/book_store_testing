# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# driver.get("http://practice.automationtesting.in/")
# driver.find_element(By.CSS_SELECTOR, "[href = 'http://practice.automationtesting.in/my-account/']").click()
# driver.find_element(By.ID, "reg_email").send_keys("britishenglish@bk.ru")
# driver.find_element(By.ID, "reg_password").send_keys("Gui12345VPN!")
# driver.find_element(By.CSS_SELECTOR, "[value = Register]").click()
# time.sleep(2)
#
# driver.quit()

from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
driver.find_element(By.CSS_SELECTOR, "[href = 'http://practice.automationtesting.in/my-account/']").click()
driver.find_element(By.ID, "username").send_keys("britishenglish@bk.ru")
driver.find_element(By.ID, "password").send_keys("Gui12345VPN!")
driver.find_element(By.CSS_SELECTOR, "[value = Login]").click()
sign_out = driver.find_element(By.CSS_SELECTOR, "[href = 'http://practice.automationtesting.in/my-account/customer-logout/']")
assert sign_out.is_displayed()
driver.quit()
