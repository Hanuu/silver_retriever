import requests
from bs4 import BeautifulSoup as bs

if __name__ =="__main__":
    simulate_url = "https://websim.worldquantvrc.com/simulate"

    login_data = LOGIN_INFO = {
        'EmailAddress': 'minjunkwakwak@gmail.com',
        'Password': 'pw',
        'next': simulate_url
    }
    session = requests.session()
    login_request = session.post("https://websim.worldquantvrc.com/sign-in", LOGIN_INFO)

    # print(login_request.status_code)
    # print(session.get(simulate_url).text)
    # csrf = session.get(simulate_url).cookies['csrftoken']
    soup = bs(session.get(simulate_url).text, "html.parser")
    csrf_key = soup.find(name = "csrf")
    # csrf_key = bs(session.get(simulate_url).text, 'html.parser').find('input', {'name': '_xsrf'})['value']

    websim_expression = "ts_rank(volume,85)"
    SIMULATION_INFO = {
        "args": [{
            "delay": "1", "unitcheck": "off", "univid": "TOP1500", "opcodetype": "FLOWSEXPR",
            "opassetclass": "EQUITY", "optrunc": 0, "code": websim_expression, "region": "ASI", "opneut": "market",
            "pasteurize": "on", "nanhandling": "on", "IntradayType": "", "tags": "equity", "decay": 0, "DataViz": 0,
            "backdays": 512, "simtime": "Y10"
        }],
        "_xsrf": csrf_key}

    sim_req = session.post(simulate_url, json=SIMULATION_INFO, headers=dict(Referer=simulate_url))
    print(sim_req.json())
    sim_res_csrf = {"_xsrf": csrf_key}
    sim_res_index = str(sim_req.json()['result'][0])

    sim_res = session.post('https://www.worldquantvrc.com/job/pnlchart/' + sim_res_index,
                     data=sim_res_csrf, headers=dict(Referer=URL))

    sim_sum = session.post('https://www.worldquantvrc.com/job/simsummary/' + sim_res_index,
                     data=sim_res_csrf, headers=dict(Referer=URL))

    sim_res.text
    print(sim_sum.text)
    print(sim_req.text)