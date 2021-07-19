# импортируем библиотеки, для того чтобы управлять браузером с помошью python
from selenium import webdriver # в данном случае это selenium(не самый быстрый вариант, но я не знаю как пользоваться requests)
from selenium.webdriver.common.keys import Keys # импортируем Keys для того чтобы мы могли отправлять какой-то текст
from datetime import date
from dateutil.relativedelta import relativedelta

driver = webdriver.Chrome('/home/zawarudo/Documents/chromedriver') # указываем питону где находится наш драйвер
driver.get('https://fetefot763.eu.pythonanywhere.com/tasks/task9') # получаем страницу с конкурсом
element = driver.find_element_by_id('user-login') # находим поле логина по его id(можно узнать из кода элемента)
element.send_keys('Kapitoshka1') # вводим наш логин
element = driver.find_element_by_id('user-pass') # находим поле пароля по его id(можно также узнать из кода элемента)
element.send_keys('RFGBNJIRF1') # вводим наш пароль
element.send_keys(Keys.ENTER) # нажимаем ENTER чтобы залогиниться
driver.get('https://fetefot763.eu.pythonanywhere.com/tasks/task9') # получаем страницу с заданием

def off0(str):
    for i in range(len(str)):
        if str[i] == '0':
            str.replace('0', '')
        else:
            break
    return str
def date2int(date):
    d, m, y = map(str, date.split('.'))
    y = int(off0(y))
    m = int(off0(m))
    d = int(off0(d))
    return y, m, d
y, m, d = 0, 0, 0
for i in range(150):
    element = driver.find_element_by_id('task-data')
    y, m, d = date2int(element.text)
    d = str(date(y, m, d)+relativedelta(days=+701)).replace('-', '.')
    element = driver.find_element_by_name('answer')
    element.send_keys(d[8:] + '.' + d[5:7] + '.' + d[0:4])
    element.send_keys(Keys.ENTER)

