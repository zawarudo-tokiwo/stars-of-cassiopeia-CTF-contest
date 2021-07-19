# импортируем библиотеки, для того чтобы управлять браузером с помошью python
from selenium import webdriver # в данном случае это selenium(не самый быстрый вариант, но я не знаю как пользоваться requests)
from selenium.webdriver.common.keys import Keys # импортируем Keys для того чтобы мы могли отправлять какой-то текст
# для того чтобы у нас все работало нужно скачать драйвер для нашего браузера, в моем случае это хром
driver = webdriver.Chrome('/home/zawarudo/Documents/chromedriver') # указываем питону где находится наш драйвер
driver.get('https://fetefot763.eu.pythonanywhere.com/tasks/task17') # получаем страницу с конкурсом
element = driver.find_element_by_id('user-login') # находим поле логина по его id(можно узнать из кода элемента)
element.send_keys('test') # вводим наш логин
element = driver.find_element_by_id('user-pass') # находим поле пароля по его id(можно также узнать из кода элемента)
element.send_keys('test') # вводим наш пароль
element.send_keys(Keys.ENTER) # нажимаем ENTER чтобы залогиниться
driver.get('https://fetefot763.eu.pythonanywhere.com/tasks/task17') # получаем страницу с заданием
element = driver.find_element_by_name('answer') # находим поле ответа по id
# нам нужно число pi, но не сказанно какой длинны, так что копируем побольше чтобы наверняка
pi = '3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975'
# пока у нас не перепробуются все знаки после запятой у нашего pi
for i in range(len(pi)):
    element.send_keys(pi[:i]) # вводим значение в поле ответа
    element.send_keys(Keys.ENTER) # и отправляем
    element = driver.find_element_by_name('answer') # так как после неверного ответа сайт перезагружается, нам нужно опять найти поле ответа
# все, программа автоматически набирает pi и отправляет его, осталось только подождать нужного символа
