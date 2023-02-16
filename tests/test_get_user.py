import requests
from pytest_voluptuous import S
from schemata.user import single_user_schema


'''Отправляем get-запрос'''

# response: Response = requests.get(url='https://reqres.in/api/users/2')
# print(response.text)
# print(response.status_code)

'''Оборачиваем запрос в тест'''


def test_get_users():
    response = requests.get(url='https://reqres.in/api/users/2')
    print(response.text)
    print(response.status_code)

    assert response.status_code == 200


'''Проверяем body респонса'''


def test_body_data():
    response = requests.get(url='https://reqres.in/api/users/2')

    assert response.json()['data']['email'] == "janet.weaver@reqres.in"


'''Проверяем наличие поля avatar'''


def test_avatar_field():
    response = requests.get(url='https://reqres.in/api/users/2')

    assert response.json().get('data').get('avatar', None)


def test_user_has_avatar():
    response = requests.get(url='https://reqres.in/api/users/2')
    avatar = response.json().get('data').get('avatar')
    result = requests.get(avatar)

    assert result.status_code == 200
    assert len(response.content) != 0
    print(len(response.content))


'''Тестируем json-схему, сами схемы вынесены в отдельный модуль user.py (библиотека voluptuous)'''


def test_get_users_schema():
    response = requests.get(url='https://reqres.in/api/users/2')

    assert response.status_code == 200
    assert S(single_user_schema) == response.json()
