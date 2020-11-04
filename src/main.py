from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from handlers import users


app = FastAPI()


async def get_token_header():
    # TODO implements
    print("implements")


app.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


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


@app.get('/')
async def main():
    return {'message': 'hello'}
