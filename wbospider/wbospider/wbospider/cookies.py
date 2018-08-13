import pymongo
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


WeiBoAccounts = [
     {'username': '13880587576', 'password': 'cs194802'},
]

cookies = []
client = pymongo.MongoClient('localhost', 27017)
db = client['Sina']
userAccount = db['userAccount']


def get_cookie_from_weibo(username, password):
    driver = webdriver.Chrome()
    driver.get('https://weibo.cn')
    try:
        assert '微博' in driver.title
    except Exception as e:  # 抛出异常
        print('Assertion test fail.', format(e))
    login_link = driver.find_element_by_link_text('登录')  # 定位登录
    ActionChains(driver).move_to_element(login_link).click().perform()  # 点击登录
    login_name = WebDriverWait(driver, 10).until(  # 等loginName刷出
        EC.invisibility_of_element_located((By.ID, 'loginName'))
    )
    login_password = driver.find_element_by_id('loginPassword')  # 定位password
    login_name.send_keys(username)
    login_password.send_keys(password)
    login_button = driver.find_element_by_id('loginAction')  # 定位登陆按钮
    login_button.click()  # 点击登录
    #  停留10秒是否登录成功,没有则手动登录
    sleep(10)
    cookie = driver.get_cookies()
    driver.close()
    return cookie


def init_cookies():
    for cookie in userAccount.find():
        cookies.append(cookie['cookie'])


if __name__ == '__main__':
    for account in WeiBoAccounts:
        cookie = get_cookie_from_weibo(account['username'], account['password'])
        userAccount.insert_one(
            {'_id': account['username'], 'cookie': cookie}
        )
