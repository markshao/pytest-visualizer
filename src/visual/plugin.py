import pytest


def pytest_addoption(parser):
    group = parser.getgroup("visual")
    group.addoption(
        "--vport",
        action="store",
        dest="vport",
        default="8080",
        help="Bind visual process port on"
    )


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    pass


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session):
    pass
