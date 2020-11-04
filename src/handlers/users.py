from fastapi import APIRouter

router = APIRouter()

fake_users = [
    {
        "id": 1,
        "name": "Aguinelo",
        "username": "aguinelo"
    },
    {
        "id": 2,
        "name": "Koczkodai",
        "username": "koczkodai"
    }
]


@router.get("/", tags=["users"])
async def all_users():
    return fake_users


@router.get("/me", tags=["users"])
async def me():
    return fake_users[0]


@router.get("/{username}", tags=["users"])
async def by_username(username: str):
    return {"username": username}
