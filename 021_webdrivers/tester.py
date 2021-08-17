from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://cv.ee/et/vacancy/610530/cloudmore-ou/software-developer-in-test-python?')

source1 = driver.page_source
print(source1)
first_info = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div/div/ul/li[2]/span')
first_info.click()
source2 = driver.page_source
print(source2)
company = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div/div/ul/li[3]/span')
company.click()
source3 = driver.page_source
print(source3)
if source1 == source2 and source2 == source3:
    print('All the same')
else:
    print('Not same')