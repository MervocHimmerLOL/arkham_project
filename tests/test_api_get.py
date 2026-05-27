import pytest

class TestGetLocations:

    @pytest.mark.positive
    @pytest.mark.asyncio  # ← обязательно для async-тестов
    async def test_get_all_locations(self, client):
        """Тест: успешное получение списка локаций"""
        resp = await client.get_locations()  # ← await + async def

        assert resp.status == 200  # ← aiohttp использует .status, не .status_code

        data = await resp.json()
        assert isinstance(data, list)  # дополнительная проверка структуры

class TestGetDetevtives:

    @pytest.mark.positive
    @pytest.mark.asyncio  # ← обязательно для async-тестов
    async def test_get_all_detectives(self, client):
        """Тест: успешное получение списка локаций"""
        resp = await client.get_detectives()  # ← await + async def

        assert resp.status == 200  # ← aiohttp использует .status, не .status_code

        data = await resp.json()
        assert isinstance(data, list)  # дополнительная проверка структуры