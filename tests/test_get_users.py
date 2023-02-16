import logging

import requests
from pytest_voluptuous import S
from schemata.user import users_list_schema


'''Проверяем json-схему для списка пользователей'''


def test_get_users_list_schema():
    result = requests.get('https://reqres.in/api/users?page=2')

    assert S(users_list_schema) == result.json()


'''Проверяем json-схему для списка пользователей с выводом в лог пользователей с 1 страницы'''


def test_get_users_list_schema_1():
    result = requests.get('https://reqres.in/api/users', params={'page': 1})
    logging.info(result.json())

    assert S(users_list_schema) == result.json()


"""Проверяем количество пользователей на странице"""


def test_count_users_per_page():
    response = requests.get('https://reqres.in/api/users', params={'page': 2})
    per_page = response.json()['per_page']
    data = response.json()['data']

    assert per_page == 6
    assert len(data) == 6      # этот ассерт необязательный, можно только per_page проверить