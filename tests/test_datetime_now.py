import datetime

import pytest

from src.datetime_now import get_now, get_now_with_timezone

FAKE_NOW = datetime.datetime(2025, 1, 1)


@pytest.fixture
def patch_datetime(monkeypatch):
    class MockDatetime:
        @classmethod
        def now(cls, tz=None):
            return FAKE_NOW

    monkeypatch.setattr(datetime, "datetime", MockDatetime)


class TestGetNow:
    def test_get_now_success(self, patch_datetime):
        assert get_now() == "2025-01-01T00:00:00"


class TestGetNowWithTimezone:
    def test_get_now_with_timezone_success(self, patch_datetime):
        assert get_now_with_timezone(timezone=datetime.timezone.utc) == "2025-01-01T00:00:00"
