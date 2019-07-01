### 풀어서 하기
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# URL = 'https://www.worldquantvrc.com/simulate'
URL = "https://websim.worldquantvrc.com/simulate"

LOGIN_INFO = {
    'EmailAddress': 'minjunkwakwak@gmail.com',
    'Password': 'pw',
    'next': URL
}

def log_in_vrc(login_info):
    simulate_url = "https://websim.worldquantvrc.com/simulate"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(simulate_url)
    driver.find_element_by_id("email").send_keys(LOGIN_INFO["EmailAddress"])

s = requests.Session()
csrf_key = bs(s.get(URL).text, 'html.parser').find('input', {'name': '_xsrf'})['value']
LOGIN_INFO['_xsrf'] = csrf_key

print(LOGIN_INFO['_xsrf'])

login_req = s.post('https://www.worldquantvrc.com/login/process', data=LOGIN_INFO)

if login_req.status_code != 200:
    raise Exception('로그인이 되지 않았어요! 아이디와 비밀번호를 다시한번 확인해 주세요.')

#########################3

websim_expression = "ts_rank(volume,85)"

csrf_key = bs(s.get(URL).text, 'html.parser').find('input', {'name': '_xsrf'})['value']

SIMULATION_INFO = {
    "args": [{
        "delay": "1", "unitcheck": "off", "univid": "TOP1500", "opcodetype": "FLOWSEXPR",
        "opassetclass": "EQUITY", "optrunc": 0, "code": websim_expression, "region": "ASI", "opneut": "market",
        "pasteurize": "on", "nanhandling": "on", "IntradayType": "", "tags": "equity", "decay": 0, "DataViz": 0,
        "backdays": 512, "simtime": "Y10"
    }],

    "_xsrf": csrf_key}

sim_req = s.post(URL, json=SIMULATION_INFO, headers=dict(Referer=URL))

# print(sim_req.text)

##############################################
sim_res_csrf = {"_xsrf": csrf_key}
sim_res_index = str(sim_req.json()['result'][0])

sim_res = s.post('https://www.worldquantvrc.com/job/pnlchart/' + sim_res_index,
                 data=sim_res_csrf, headers=dict(Referer=URL))

sim_sum = s.post('https://www.worldquantvrc.com/job/simsummary/' + sim_res_index,
                 data=sim_res_csrf, headers=dict(Referer=URL))

sim_res.text
print(sim_sum.text)

#####################################
SUBMIT_INFO = {
    '_xsrf': '2|538314d0|e8b61b830647c10e3345b7492ba65007|1543968707',
    'args': {"alpha_list": ["0be80e9d2ab144619f82c5ddd27d383f"]}
}
SUBMIT_INFO = json.loads(json.dumps(SUBMIT_INFO))

sim_check = s.post('https://www.worldquantvrc.com/submission/start', json=SUBMIT_INFO,
                   headers=dict(Referer='https://www.worldquantvrc.com/alpha/0be80e9d2ab144619f82c5ddd27d383f'))

sim_check.text

sim_check = s.get('https://www.worldquantvrc.com/submission/start', json=SUBMIT_INFO,
                  headers=dict(Referer='https://www.worldquantvrc.com/alpha/0be80e9d2ab144619f82c5ddd27d383f'))

sim_check.json