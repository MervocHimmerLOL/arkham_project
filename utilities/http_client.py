# api_client.py
import aiohttp
from typing import Optional


class ApiClient:
    """Простой асинхронный HTTP-клиент (только запросы, без бизнес-логики)"""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self._session: Optional[aiohttp.ClientSession] = None

    async def _get_session(self) -> aiohttp.ClientSession:
        """Ленивая инициализация сессии"""
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
        return self._session

    async def get_locations(self):
        """GET /locations — возвращает aiohttp.ClientResponse"""
        session = await self._get_session()
        return await session.get(f"{self.base_url}/locations")

    async def get_detectives(self):
        """GET /detectives — возвращает aiohttp.ClientResponse"""
        session = await self._get_session()
        return await session.get(f"{self.base_url}/detectives")

    async def close(self):
        """Закрыть сессию (вызывать при завершении работы)"""
        if self._session and not self._session.closed:
            await self._session.close()