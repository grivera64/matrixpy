import pytest
from unittest.mock import Mock
from nio import MatrixRoom

from matrix.broadcast_result import BroadcastResult
from matrix.errors import MatrixError
from matrix.message import Message


@pytest.fixture
def room():
    return Mock(spec=MatrixRoom)


@pytest.fixture
def message():
    return Mock(spec=Message)


def test_ok__with_no_error__expect_true(room, message):
    result = BroadcastResult(room=room, message=message, error=None)

    assert result.ok


def test_ok__with_error__expect_false(room):
    result = BroadcastResult(room=room, message=None, error=MatrixError("boom"))

    assert not result.ok
