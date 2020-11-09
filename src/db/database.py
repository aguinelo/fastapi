from config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT, MONGODB_DATABASE
import motor
from motor.motor_asyncio import AsyncIOMotorClient


class Database():
    def get_client(self) -> AsyncIOMotorClient:
        return AsyncIOMotorClient(MONGODB_URL)[MONGODB_DATABASE]
