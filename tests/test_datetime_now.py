import datetime

import pytest

FAKE_NOW = datetime.datetime(2025, 1, 1, 12, 0, 0)


@pytest.fixture()
def patch_datetime(mocker, monkeypatch):
    """
    Patch datetime
    """
    mocked_datetime = mocker.MagicMock(wrapt=datetime.datetime)
    mocked_datetime.now.return_value = FAKE_NOW

    monkeypatch.setattr(datetime, "datetime", mocked_datetime)


def test_datetime_now(patch_datetime):
    """
    Test datetime now without timezone
    """
    assert datetime.datetime.now() == FAKE_NOW


def test_datetime_now_with_timezone(patch_datetime):
    """
    Test datetime now with timezone
    """
    assert datetime.datetime.now(tz=datetime.timezone.utc) == FAKE_NOW
