import pytest
from fastapi.testclient import TestClient
from pms.main import app

@pytest.fixture()
def client():
    return TestClient(app)
