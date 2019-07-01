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
    input("wait")

if __name__ == "__main__":
    URL = "https://websim.worldquantvrc.com/simulate"
    LOGIN_INFO = {
        'EmailAddress': 'minjunkwakwak@gmail.com',
        'Password': 'pw',
        'next': URL
    }
    log_in_vrc(LOGIN_INFO)