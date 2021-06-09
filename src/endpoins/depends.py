from repositories.devices import DeviceRepository
from db.base import databases


def get_device_repository() -> DeviceRepository:
    return DeviceRepository(databases)