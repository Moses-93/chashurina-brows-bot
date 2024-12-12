import logging
from aiocache import caches
from abc import ABC, abstractmethod


logger = logging.getLogger(__name__)


class ICache(ABC):

    @abstractmethod
    async def get(self, key: str):
        pass

    @abstractmethod
    async def set(self, key: str, value):
        pass

    @abstractmethod
    async def delete(self, key: str):
        pass


class AioCacheAdapter(ICache):

    def __init__(self, caches_name="users_cache") -> None:
        self._cache = caches.get(caches_name)

    async def get(self, key: str):
        try:
            return await self._cache.get(key)
        except KeyError:
            logger.error(f"Помилка доступу до кешу: {key}")

    async def set(self, key: str | int, value):
        await self._cache.set(key, value)
        logger.info(f"Кеш оновлено: {key} -> {value}")

    async def delete(self, key: str | int):
        await self._cache.delete(key)
        logger.debug(f"Ключ видалено з кешу: {key}")
