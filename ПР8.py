import requests
# Завдання 1
response = requests.get('https://www.example.com')
print(response.text)

# Завдання 2
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://httpbin.org/get', params=params)
print(response.url)

# Завдання 3
data = {'username': 'myuser', 'password': 'mypassword'}
response = requests.post('https://httpbin.org/post', data=data)
print(response.json())

# Завдання 4
print(response.status_code)
print(response.headers)

# Завдання 5
try:
    response = requests.get('https://www.example.com/nonexistent')
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f'Помилка: {e}')

# Завдання 6
with open('example.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
