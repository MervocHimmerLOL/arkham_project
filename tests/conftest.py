import pytest
import pytest_asyncio

from utilities.http_client import ApiClient

@pytest_asyncio.fixture
async def client():
    """Фикстура: создаёт и закрывает ApiClient для тестов"""
    api = ApiClient(base_url="http://localhost:8000")
    yield api
    await api.close()