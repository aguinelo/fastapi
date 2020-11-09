from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel, Field
from bson import ObjectId

from db.database import Database

app = FastAPI()


# CORS handler
origins = [
    "http://localhost.aguinelo.com",
    "https://localhost.aguinelo.com",
    "http://localhost",
    "http://localhost:8000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise ValueError("Not a valid ObjectId")
        return str(v)


class MyModel(BaseModel):
    id: ObjectIdStr = Field(..., alias="_id")
    name: str
    logo: str


@app.get('/')
async def main():
    return {'message': 'hello'}


@app.get("/teste", tags=["teste"])
async def teste():
    db = Database().get_client()

    return await get_brands(db)


async def get_brands(db) -> list[MyModel]:
    res = []
    _list = await db.brands.find({}).to_list(None)

    for i in _list:
        res.append(MyModel(**i))

    return res
