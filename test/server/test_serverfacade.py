import logging
from mock import MagicMock
import pytest
from syncloud.app import logger
from syncloud.server.serverfacade import ServerFacade

logger.init(logging.DEBUG, True)


@pytest.fixture(scope="session")
def sam():
    sam = MagicMock()
    sam.update = MagicMock(return_value=True)
    sam.upgrade_all = MagicMock(return_value=True)
    return sam


@pytest.fixture(scope="session")
def insider():
    insider = MagicMock()
    insider.set_redirect_info = MagicMock(return_value=True)
    insider.acquire_domain = MagicMock(return_value=True)
    return insider

@pytest.fixture(scope="session")
def remote():
    remote = MagicMock()
    remote.enable = MagicMock(return_value='key123')
    return remote

@pytest.fixture(scope="session")
def apache():
    apache = MagicMock()
    apache.activate = MagicMock()
    return apache


def test_activate_good(sam, insider, remote, apache):

    server = ServerFacade(sam, insider, remote, apache)
    credentials = server.activate('0.1', 'syncloud.it', 'http://api.syncloud.it', 'test@example.com', 'pass123', 'test')

    assert credentials.key == 'key123'


def test_activate_bad(sam, insider, remote, apache):

    remote.enable = Exception('Boom!')

    server = ServerFacade(sam, insider, remote, apache)

    with pytest.raises(Exception):
        server.activate('0.1', 'syncloud.it', 'http://api.syncloud.it', 'test@example.com', 'pass123', 'test')