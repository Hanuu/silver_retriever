from selenium import webdriver


def log_in_vrc(login_info):
    simulate_url = "https://websim.worldquantvrc.com/simulate"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(simulate_url)
    driver.find_element_by_id("email").send_keys(str(login_info["EmailAddress"]))
    driver.find_element_by_id("password").send_keys(str(login_info["Password"]))
    driver.find_element_by_xpath('//*[@id="root"]/div/section/div/article/div/div/form/div[4]/button').click()

    while(True):
        try:
            driver.find_element_by_xpath('/html/body/div[6]/div/div[5]/a[1]').click()
        except:
            pass
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div/div[1]/div/div[1]/div[2]/div[1]/div[4]/div/span/span').send_keys("I am the destructor")
if __name__ == "__main__":
    LOGIN_INFO = {
        'EmailAddress': 'minjunkwakwak@gmail.com',
        'Password': '',
    }
    log_in_vrc(LOGIN_INFO)