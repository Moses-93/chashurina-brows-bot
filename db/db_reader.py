from aiocache import cached

from .repository import (
    BaseGetNotes,
    BaseGetServices,
    BaseGetDates,
    BaseGetAdmins,
    base_get_notes,
    base_get_service,
    base_get_free_date,
    base_get_admins,
)


class GetNotes:

    def __init__(self, notes: BaseGetNotes):
        self.notes = notes

    async def get_notes(self, *expressions, **filters):
        result = await self.notes.get_notes(*expressions, **filters)
        return result


class GetServices:

    def __init__(self, services: BaseGetServices):
        self.services = services

    @cached(ttl=1800, alias="queries_cache")
    async def get_service(self, first=False, **filters):
        result = await self.services.get_service(**filters)
        if first and result:
            return result[0]
        return result


class GetDates:

    def __init__(self, dates: BaseGetDates):
        self.dates = dates

    @cached(ttl=1800, alias="queries_cache")
    async def get_date(self, first=False, **filters):
        result = await self.dates.get_date(**filters)
        if first and result:
            return result[0]
        return result


class GetAdmins:

    def __init__(self, admins: BaseGetAdmins):
        self.admins = admins

    @cached(ttl=1800, alias="queries_cache")
    async def get_admins(self, first=False, **filters):
        print("Запит в базу для читання")
        result = await self.admins.get_admins(**filters)
        if first and result:
            return result[0]
        return result


get_admins = GetAdmins(base_get_admins)
get_notes = GetNotes(base_get_notes)
get_services = GetServices(base_get_service)
get_dates = GetDates(base_get_free_date)
