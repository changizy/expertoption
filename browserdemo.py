import time
from selenium import webdriver

driver = webdriver.Chrome('/home/toor/Desktop/Option/chromedriver')
driver.get('https://expertoption.com/?demo=true')
time.sleep(20)
#webdriver.findElement(By.linkText("deal-button call")).click()
# webdriver.driver.findElement(By.CLASS_NAME("deal-button call")).click()
#prof = 0 
#while prof == 0:
driver.find_element_by_class_name("call").click()
time.sleep(80)

#click(findElement.By.linkText("deal-button call"))
prof = driver.find_element_by_class_name("currency")
print(prof)
print(driver.title)
#time.sleep(80)
driver.quit()
