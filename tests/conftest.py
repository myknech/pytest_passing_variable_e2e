import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--baseurl", action="store", default="http://localhost:4567", help="base api url"
    )


@pytest.fixture()
def conf_baseurl(request):
    return request.config.getoption("--baseurl")
