from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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


@app.get('/')
async def main():
    return {'message': 'hello'}
