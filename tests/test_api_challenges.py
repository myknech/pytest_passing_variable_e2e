import json

import pytest
from assertpy import assert_that
from requests import *

baseurl = ''
x_challenger = ''
base_headers = {}


@pytest.fixture(autouse=True)
def set_baseurl(conf_baseurl):
    global baseurl
    if baseurl == '':
        baseurl = conf_baseurl


@pytest.fixture(autouse=True)
def set_base_headers(set_baseurl):
    global x_challenger, base_headers
    if x_challenger == '':
        response = get(f"{baseurl}/challenger")
        x_challenger = response.headers['x-challenger']
    if base_headers == {}:
        base_headers['X-CHALLENGER'] = x_challenger


@pytest.mark.order(1)
def test_get_x_challenger_header():
    assert_that(x_challenger).is_equal_to('rest-api-challenges-single-player')


@pytest.mark.order(2)
def test_get_challenges():
    response = get(f"{baseurl}/challenges")

    response_json_dict = json.loads(response.content)

    challenge_02_dict = response_json_dict['challenges'][1]

    print(challenge_02_dict)

    assert_that(challenge_02_dict['description']).is_equal_to('Issue a GET request on the `/challenges` end point')
    assert_that(challenge_02_dict['status']).is_equal_to(True)


@pytest.mark.order(3)
def test_get_todos():
    response = get(f"{baseurl}/todos", headers=base_headers)
    print()
    json_dict: dict = json.loads(response.text)
    dict_list: list = json_dict['todos']
    print(dict_list)
