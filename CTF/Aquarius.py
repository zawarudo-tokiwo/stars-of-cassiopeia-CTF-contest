# импортируем библиотеки, для того чтобы управлять браузером с помошью python


 # импортируем Keys для того чтобы мы могли отправлять какой-то текст
import time
# для того чтобы у нас все работало нужно скачать драйвер для нашего браузера, в моем случае это хром
driver = webdriver.Chrome('/home/zawarudo/Documents/chromedriver') # указываем питону где находится наш драйвер
driver.get('https://fetefot763.eu.pythonanywhere.com/tasks/task1') # получаем страницу с конкурсом
element = driver.find_element_by_id('user-login') # находим поле логина по его id(можно узнать из кода элемента)
element.send_keys('Kapitoshka1') # вводим наш логин
element = driver.find_element_by_id('user-pass') # находим поле пароля по его id(можно также узнать из кода элемента)
element.send_keys('RFGBNJIRF1') # вводим наш пароль
element.send_keys(Keys.ENTER) # нажимаем ENTER чтобы залогиниться
driver.get('https://fetefot763.eu.pythonanywhere.com/tasks/task1') # получаем страницу с заданием

# функция подсчёта слов
def count_words(s):
    alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    s = s.replace('?', ' ')
    s = s.replace('!', ' ')
    s = s.replace('.', ' ')
    s = s.replace(',', ' ')
    s = s.replace('-', ' ')
    s = s.replace('_', ' ')
    #for i in range(len(alp)):
    #    s = s.replace(' ' + alp[i] + ' ', ' ')
    s = s.split()
    return len(s)




while True:
    str = driver.find_element_by_id('task-data').text
    element = driver.find_element_by_name('answer')
    element.send_keys(count_words(str))
    element.send_keys(Keys.ENTER)



