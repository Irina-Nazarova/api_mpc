from typing import List
from fastapi import APIRouter, Depends
from repositories.users import UserRepository
from models.users import User, UserIn
from .depends import get_user_repository

router = APIRouter()


@router.get("/", response_model=List[User])
async def read_users(users: UserRepository = Depends(get_user_repository), limit: int = 100, skip: int = 100):
    # TODO: Убрать захешированый пароль из ответа
    return await users.get_all(limit=limit, skip=0)


@router.post("/", response_model=User)
async def create_user(
        user: UserIn,
        users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=user)


@router.put("/", response_model=User)
async def update_user(
    id: int,
    user: UserIn,
    users: UserRepository = Depends(get_user_repository)):
    return await users.update(id=id, u=user)

