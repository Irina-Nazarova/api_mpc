from typing import List, Optional

from models.devices import Device, DeviceIn
from db.devices import devices
from .base import BaseRepository


class DeviceRepository(BaseRepository):

    async def get_device_by_id(self, id: int) -> Optional[Device]:
        query = devices.select().where(devices.c.id == id)
        return await self.database.fetch_one(query)

    async def get_device_by_ip_address(self, ip_address: str) -> List[Device]:
        query = devices.select().where(devices.c.ip_address == ip_address)
        return await self.database.fetch_all(query=query)

    async def get_device_by_hostname(self, hostname: str) -> List[Device]:
        query = devices.select().where(devices.c.hostname == hostname)
        return await self.database.fetch_all(query=query)

    async def get_all_device(self, limit: int = 100, skip: int = 0) -> List[Device]:
        query = devices.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def create_device(self, d: DeviceIn) -> Device:
        device = Device(
            ip_address=d.ip_address,
            hostname=d.hostname,
            model=d.model,
        )
        values = {**device.dict()}
        values.pop("id", None)
        query = devices.insert().values(**values)
        device.id = await self.database.execute(query)
        return device

    async def update_device(self, id: int, d: DeviceIn) -> Device:
        device = Device(
            ip_address=d.ip_address,
            hostname=d.hostname,
            model=d.model,
        )
        values = {**device.dict()}
        values.pop("id", None)
        query = devices.update().where(devices.c.id == id).values(**values)
        await self.database.execute(query=query)
        return device

    async def delete_device(self, id: int):
        query = devices.delete().where(devices.c.id == id)
        return await self.database.execute(query=query)