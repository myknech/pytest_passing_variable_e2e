from requests import *

base_url = 'http://localhost:9000'


def test_basic():
    response = get(f"{base_url}/todo/items")

    print("\n", response)
