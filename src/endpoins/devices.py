from typing import List, Optional

from fastapi import APIRouter, Depends
from repositories.devices import DeviceRepository
from models.devices import Device, DeviceIn
from .depends import get_device_repository


router = APIRouter()


@router.get("/id/{id}", response_model=Device)
async def get_device_by_id(
        id: int,
        devises: DeviceRepository = Depends(get_device_repository)):
    return await devises.get_device_by_id(id=id)


@router.get("/ip/{ip}", response_model=List[Device])
async def get_device_by_ip(
        ip_address: str,
        devises: DeviceRepository = Depends(get_device_repository)):
    return await devises.get_device_by_ip_address(ip_address=ip_address)


@router.get("/{hostname}", response_model=List[Device])
async def get_device_by_hostname(
        hostname: str,
        devises: DeviceRepository = Depends(get_device_repository)):
    return await devises.get_device_by_hostname(hostname=hostname)


@router.get("/", response_model=List[Device])
async def get_devices(
        devices: DeviceRepository = Depends(get_device_repository),
        limit: int = 100,
        skip: int = 0):
    return await devices.get_all_device(limit=limit, skip=skip)


@router.post("/", response_model=Device)
async def create_device(
        device: DeviceIn,
        devices: DeviceRepository = Depends(get_device_repository)):
    return await devices.create_device(d=device)


@router.put("/", response_model=Device)
async def update_device(
        id: int,
        device: DeviceIn,
        devices: DeviceRepository = Depends(get_device_repository)):
    return await devices.update_device(id=id, d=device)


@router.delete("/")
async def delete_device(id: int, devices: DeviceRepository = Depends(get_device_repository)):
    return await devices.delete_device(id=id)


