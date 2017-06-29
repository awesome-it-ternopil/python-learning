from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://accounts.google.com/Login/identifier?flowName=GlifWebSignIn&flowEntry=AddSession")
driver.implicitly_wait(5)
driver.find_element_by_id("identifierId").send_keys("arsen.senyk@gmail.com")
driver.implicitly_wait(5)
driver.find_element_by_id("identifierNext").click()
driver.implicitly_wait(5)
driver.find_element("name","password").send_keys("AAAAAbbbbb")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//div[@role='button'][@id='passwordNext']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//a[@class='WaidBe'][@data-track-as='Welcome Header Mail']").click()
driver.implicitly_wait(5)





