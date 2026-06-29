from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module

BASELINE_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities(monkeypatch):
    """Reset mutable in-memory activity data before each test."""
    monkeypatch.setattr(app_module, "activities", deepcopy(BASELINE_ACTIVITIES))


@pytest.fixture
def client(reset_activities):
    """Create an isolated FastAPI test client for each test."""
    with TestClient(app_module.app) as test_client:
        yield test_client
