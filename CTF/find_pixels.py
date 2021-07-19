from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
import urllib.request
from math import sqrt

driver = webdriver.Chrome('/home/zawarudo/Documents/chromedriver')
driver.get('https://fetefot763.eu.pythonanywhere.com/tasks/task43')
element = driver.find_element_by_id('user-login')
element.send_keys('Kapitoshka1')
element = driver.find_element_by_id('user-pass')
element.send_keys('RFGBNJIRF1')
element.send_keys(Keys.ENTER)
driver.get('https://fetefot763.eu.pythonanywhere.com/tasks/task43')

def right_coords(coords):
    x1, y1 = coords[0]
    x2, y2 =coords[1]

    if x1 > x2:
        x1 -= 0.5
        x2 += 0.5
    elif x1 < x2:
        x1 += 0.5
        x2 -= 0.5

    if y1 > y2:
        y1 -= 0.5
        y2 += 0.5
    elif y1 < y2:
        y1 += 0.5
        y2 -= 0.5
    return [(x1, y1), (x2, y2)]

def get_coords(i):
    # получаем картинку
    img_src = driver.find_element_by_xpath('//div[@id="task-data"]/img')
    src = img_src.get_attribute('src')
    # скачиваем картинку
    urllib.request.urlretrieve(src, f"{i}.png")
    # открываем её
    img = Image.open(f"{i}.png")
    pixels = img.load()
    width, height = img.size
    coords = []
    for x in range(width):
        for y in range(height):
            if pixels[x, y] == (0, 0, 0):
                coords.append((x, y))
    return coords


def count_length(x1, y1, x2, y2):
    ans = sqrt((x1-x2)**2 + (y1-y2)**2)
    if str(ans)[-1] == '0':
        return int(ans)
    else:
        return str(round(ans, 5))



for i in range(100):
    coords = get_coords(i)
    coords = right_coords(coords)
    x1, y1 = coords[0]
    x2, y2 = coords[1]
    answer = count_length(x1, y1, x2, y2)
    # отправляем его
    element = driver.find_element_by_name('answer')
    element.send_keys(answer)
    element.send_keys(Keys.ENTER)

