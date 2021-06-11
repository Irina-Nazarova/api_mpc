from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status

from endpoins.depends import get_user_repository, get_current_user
from models.users import User, UserIn
from repositories.users import UserRepository



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
    users: UserRepository = Depends(get_user_repository),
    current_user: User = Depends(get_current_user)
    ):

    old_user: Optional[User] = await users.get_by_id(id=id)
    if old_user is None or old_user.email != current_user.email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")
    return await users.update(id=id, u=user)


