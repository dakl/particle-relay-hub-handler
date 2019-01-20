from unittest.mock import Mock

from app.accessory.relay import Relay


def create_mocks():
    request_factory = Mock(spec=['create'])
    request_factory.create.return_value = {'return_value': 0}

    return {'request_factory': request_factory}


def test_set_state_calls_request_factory_once():
    mocks = create_mocks()
    r = Relay(name='', internal_id='', **mocks)

    r.set_state(1)

    mocks['request_factory'].create.assert_called_once()


def test_get_state_calls_request_factory_once():
    mocks = create_mocks()
    r = Relay(name='', internal_id='', **mocks)

    r.get_state()

    mocks['request_factory'].create.assert_called_once()
