'''4й тест'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# driver.get("http://practice.automationtesting.in/")
# driver.find_element(By.CSS_SELECTOR, "[href = 'http://practice.automationtesting.in/my-account/']").click()
# driver.find_element(By.ID, "username").send_keys("britishenglish@bk.ru")
# driver.find_element(By.ID, "password").send_keys("Gui12345VPN!")
# driver.find_element(By.CSS_SELECTOR, "[value = Login]").click()
# driver.find_element(By.LINK_TEXT, "Shop").click()
# driver.find_element(By.CSS_SELECTOR, "[alt='Mastering HTML5 Forms']").click()
# title = driver.find_element(By.CLASS_NAME,"product_title")
# assert title.text == "HTML5 Forms"
# driver.quit()

'''5-й тест'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# driver.get("http://practice.automationtesting.in/")
# driver.find_element(By.CSS_SELECTOR, "[href = 'http://practice.automationtesting.in/my-account/']").click()
# driver.find_element(By.ID, "username").send_keys("britishenglish@bk.ru")
# driver.find_element(By.ID, "password").send_keys("Gui12345VPN!")
# driver.find_element(By.CSS_SELECTOR, "[value = Login]").click()
# driver.find_element(By.LINK_TEXT, "Shop").click()
# driver.find_element(By.CSS_SELECTOR, "[href='http://practice.automationtesting.in/product-category/html/']").click()
# html_showcase = driver.find_elements(By.CLASS_NAME, "type-product")
# assert len(html_showcase) == 3
# driver.quit()

'''6-й тест'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# driver.get("http://practice.automationtesting.in/")
# driver.find_element(By.CSS_SELECTOR, "[href = 'http://practice.automationtesting.in/my-account/']").click()
# driver.find_element(By.ID, "username").send_keys("britishenglish@bk.ru")
# driver.find_element(By.ID, "password").send_keys("Gui12345VPN!")
# driver.find_element(By.CSS_SELECTOR, "[value = Login]").click()
# driver.find_element(By.LINK_TEXT, "Shop").click()
# default_order = driver.find_element(By.CSS_SELECTOR, "[value = 'menu_order']")
# default = default_order.get_attribute("selected")
# ''' Здесь и далее: ASSERT отказался работать наотрез! строка assert default == "selected" показала ошибку ассёрта,
# как и вариант с True. Поэтому далее проверка сортировки через if-else, и она работает как надо'''
# if default is not None:
#     print("Выставлена сортировка по умолчанию")
# else:
#     print("НЕ выставлена сортировка по умолчанию")
# ordering = driver.find_element(By.CLASS_NAME, "orderby")
# grouping_selection = Select(ordering)
# grouping_selection.select_by_value("price-desc")
# descending = driver.find_element(By.CSS_SELECTOR, "[value = 'price-desc']").get_attribute("selected")
# if descending is not None:
#     print("Сортировка от дорогого к дешевому установлена успешно")
# else:
#     print("Не получилось установить сортировку от дорогого к дешевому")
# driver.quit()

'''7-й тест'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# driver.find_element(By.CSS_SELECTOR, "[href = 'http://practice.automationtesting.in/my-account/']").click()
# driver.find_element(By.ID, "username").send_keys("britishenglish@bk.ru")
# driver.find_element(By.ID, "password").send_keys("Gui12345VPN!")
# driver.find_element(By.CSS_SELECTOR, "[value = Login]").click()
# driver.find_element(By.LINK_TEXT, "Shop").click()
# driver.find_element(By.CSS_SELECTOR, "[title = 'Android Quick Start Guide']").click()
# previous_price = driver.find_element(By.CSS_SELECTOR, "del > .woocommerce-Price-amount.amount").text
# assert previous_price == "₹600.00"
# actual_price = driver.find_element(By.CSS_SELECTOR, "ins > .woocommerce-Price-amount.amount").text
# assert actual_price == "₹450.00"
# wait = WebDriverWait(driver,10)
# driver.find_element(By.CSS_SELECTOR, "[itemprop = 'image']").click()
# '''пункты 7-8: Не удалось сделать так, чтобы картинка обложки открывалась в режиме предпросмотра, потому что в
# автоматическом режиме он сразу открывает полноэкранную картинку. И даже если вручную в окне, открытом вебдрайвером,
# нажимать на просмотр обложки, он сразу открывает полноэкранную обложку, и там нет кнопки возврата на "предпросмотр"(!)
# А если самостоятельно заходить на сайт и открывать ту же самую обложку, обложка открывается как надо, в предпросмотре и
# с возможностью увеличения картинки. Разные селекторы перепробовал - ничего не помогло)'''
# driver.quit()

'''8-й тест'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# driver.get("http://practice.automationtesting.in/")
# driver.find_element(By.LINK_TEXT, "Shop").click()
# driver.find_element(By.CSS_SELECTOR, "[data-product_id = '182']").click()
# wait = WebDriverWait(driver, 10)
# wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "cartcontents"), "1 Item"))
# cart_indicator = driver.find_element(By.CLASS_NAME, "cartcontents")
# cart_indicator_value = cart_indicator.text
# assert cart_indicator_value == "1 Item"
# cart_price = driver.find_element(By.CLASS_NAME, "amount")
# cart_price_sum = cart_price.text
# assert cart_price_sum == "₹180.00"
# driver.find_element(By.CLASS_NAME, "wpmenucart-contents").click()
# wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title = 'Subtotal']>span"),"₹180.00"))
# wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "strong > .amount"), "₹189.00"))
# driver.quit()

'''9-й тест'''
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# import time
# driver.get("http://practice.automationtesting.in/")
# driver.find_element(By.LINK_TEXT, "Shop").click()
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element(By.CSS_SELECTOR, "[data-product_id = '182']").click()
# time.sleep(0.5)
# driver.find_element(By.CSS_SELECTOR, "[data-product_id = '180']").click()
# driver.find_element(By.CLASS_NAME, "wpmenucart-contents").click()
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, "[data-product_id = '182']").click()
# driver.find_element(By.LINK_TEXT, "Undo?").click()
# driver.find_element(By.NAME, "cart[045117b0e0a11a242b9765e79cbf113f][qty]").clear()
# driver.find_element(By.NAME, "cart[045117b0e0a11a242b9765e79cbf113f][qty]").send_keys(3)
# driver.find_element(By.NAME, "update_cart").click()
# book_quantity = driver.find_element(By.NAME, "cart[045117b0e0a11a242b9765e79cbf113f][qty]").get_attribute("value")
# assert book_quantity == "3"
# time.sleep(1)
# driver.find_element(By.NAME, "apply_coupon").click()
# assert driver.find_element(By.CLASS_NAME, "woocommerce-error").text == "Please enter a coupon code."
# driver.quit()

'''10-й тест'''
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
import time
driver.get("http://practice.automationtesting.in/")
driver.find_element(By.LINK_TEXT, "Shop").click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element(By.CSS_SELECTOR, "[data-product_id = '182']").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "wpmenucart-contents").click()
time.sleep(1)
checkout = driver.find_element(By.CSS_SELECTOR, "[href='http://practice.automationtesting.in/checkout/']")
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable(checkout))
checkout.click()
first_name_input = driver.find_element(By.ID, "billing_first_name")
wait.until(EC.element_to_be_clickable(first_name_input))
first_name_input.send_keys("Matthew")
driver.find_element(By.ID, "billing_last_name").send_keys("Seppuku")
driver.find_element(By.ID, "billing_email").send_keys("britishenglish@bk.ru")
driver.find_element(By.ID, "billing_phone").send_keys("+7 (999) 999-9999")
driver.find_element(By.CLASS_NAME, "select2-chosen").click()
driver.find_element(By.ID, "s2id_autogen1_search").send_keys("Ireland")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "select2-result-label").click()
time.sleep(1)
driver.find_element(By.ID, "billing_address_1").send_keys("Ale Street")
driver.find_element(By.ID, "billing_city").send_keys("Dublin")
driver.find_element(By.ID, "billing_state").send_keys("Dublin")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
driver.find_element(By.ID, "payment_method_cheque").click()
driver.find_element(By.ID, "place_order").click()
wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method > strong"), "Check Payments"))
time.sleep(1)
driver.quit()