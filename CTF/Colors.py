from matplotlib import colors
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
import  PIL.ImageOps
# запускаем дравер, логинимся и прочее говно
driver = webdriver.Chrome('/home/zawarudo/Documents/chromedriver')
driver.get('https://fetefot763.eu.pythonanywhere.com/tasks/task29') # получаем страницу с конкурсом
element = driver.find_element_by_id('user-login') # находим поле логина по его id(можно узнать из кода элемента)
element.send_keys('Kapitoshka1') # вводим наш логин
element = driver.find_element_by_id('user-pass') # находим поле пароля по его id(можно также узнать из кода элемента)
element.send_keys('RFGBNJIRF1') # вводим наш пароль
element.send_keys(Keys.ENTER)
driver.get('https://fetefot763.eu.pythonanywhere.com/tasks/task29')

# функция делающая из rgb hex
def rgb_to_hex(r, g, b):
    return '#%02x%02x%02x' % (r, g, b)

# переменная с картинкой
img = 0
# переменная с цветом
color = 0
inverted_color = 0
r, g, b = 0, 0, 0
# цикл на сто раз
for i in range(100):
    # получаем картинку
    img_src = driver.find_element_by_xpath('//div[@id="task-data"]/img')
    src = img_src.get_attribute('src')
    # скачиваем картинку
    urllib.request.urlretrieve(src, f"{i}.png")
    # открываем её
    obj = PIL.Image.open(f"{i}.png")
    img = obj.load()
    # получаем цвет пикселя
    color = img[0, 0]

    # инвертируем его
    inverted_color = (255 - color[0], 255 - color[1], 255 - color[2])
    # разбиваем на rgb
    r, g, b = inverted_color[0], inverted_color[1], inverted_color[2]
    # получаем инвертированный hex и чтобы он был с заглавными буквами
    inverted_color = rgb_to_hex(r, g, b).upper()

    # отправляем его
    element = driver.find_element_by_name('answer')
    element.send_keys(inverted_color)
    element.send_keys(Keys.ENTER)
