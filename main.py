from websim_login import log_in_vrc
from write_expression import write_fast_expression

if __name__ == "__main__":
    LOGIN_INFO = {
        'EmailAddress': 'minjunkwakwak@gmail.com',
        'Password': '',
    }
    log_in_vrc(LOGIN_INFO)
    write_fast_expression("I am the destructor")
