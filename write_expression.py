from selenium import webdriver


def write_fast_expression(expression_in_str):
    driver = webdriver.Chrome()
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div/div[1]/div/div[1]/div[2]/div[1]/div[4]/div/span/span').send_keys(expression_in_str)