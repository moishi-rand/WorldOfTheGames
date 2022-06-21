from selenium import webdriver
from selenium.webdriver.common.by import By

#Test of score service
def test_scores_service(url):
    #Change path of web driver on other client
    my_driver = webdriver.Chrome(executable_path=r'C:\Users\randm\Projects\chromedriver.exe')
    my_driver.get(url)
    score = int(my_driver.find_element(By.XPATH,'//*[@id="score"]').text)

    if(type(score) == type(0) and (score > 0 and score < 1001)):
        return True

    return False

#Aplly test of score service
def main_function():
    #Change url on other service
    if test_scores_service(r'http://127.0.0.1:5000'):
        return 0

    return -1

