import requests
url = 'https://fetefot763.eu.pythonanywhere.com/auth'
data = {
    'login' : 'Kapitoshka1',
    'password' : 'RFGBNJIRF1'
}

s = requests.Session()

r = s.post(url, data=data)

d = dict(s.cookies)
d['tea'] = 'ready'
print(d)

r = s.post('https://fetefot763.eu.pythonanywhere.com/tasks/task21', cookies=d)

print(r.text)