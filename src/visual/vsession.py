import pytest

PLUGIN_NAME = "vsession"


class VSession(object):

    def __init__(self):
        pass

    def pytest_sessionstart(self, session):
        pass

    def pytest_collection_modifyitems(self, session, config, items):
        pass
