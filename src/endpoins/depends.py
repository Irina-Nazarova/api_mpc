from repositories.devices import DeviceRepository
from repositories.users import UserRepository
from db.base import databases


def get_device_repository() -> DeviceRepository:
    return DeviceRepository(databases)


def get_user_repository() -> UserRepository:
    return UserRepository(databases)

