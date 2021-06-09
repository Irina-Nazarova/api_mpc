from typing import Optional
from pydantic import BaseModel


class Device(BaseModel):
    id: Optional[int] = None
    # TODO: IPAddress (IPv4, IPv6) validator
    ip_address: str
    hostname: str
    model: str


class DeviceIn(BaseModel):
    """ Data from API clients: POST, PUT """
    # TODO: IPAddress (IPv4, IPv6) validator
    ip_address: str
    hostname: str
    model: str


