import json

import pytest
from assertpy import assert_that
from requests import *

x_challenger = ''


def setup_module(baseurl):
    pass

@pytest.mark.order(1)
def test_get_x_challenger_header(baseurl):
    global x_challenger
    response = get(f"{baseurl}/challenger")

    x_challenger = response.headers['x-challenger']

    assert_that(x_challenger).is_equal_to('rest-api-challenges-single-player')


@pytest.mark.order(2)
def test_challengers(baseurl):
    response = get(f"{baseurl}/challenges")

    response_json_dict = json.loads(response.content)

    challenge_02_dict = response_json_dict['challenges'][1]

    print(challenge_02_dict)

    assert_that(challenge_02_dict['description']).is_equal_to('Issue a GET request on the `/challenges` end point')
    assert_that(challenge_02_dict['status']).is_equal_to(True)
