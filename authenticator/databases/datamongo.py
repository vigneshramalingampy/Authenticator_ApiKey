
from beanie import init_beanie
import motor.motor_asyncio

from authenticator.model.auth_key_model import AuthKey
from authenticator.model.dbmodel import Book


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://localhost:27017"
    )
    print("hai")
    await init_beanie(database=client.db_name, document_models=[Book,AuthKey])

# api_keys = {
#         "e54d4431-5dab-474e-b71a-0db1fcb9e659": "7oDYjo3d9r58EJKYi5x4E8",
#         "5f0c7127-3be9-4488-b801-c7b6415b45e9": "mUP7PpTHmFAkxcQLWKMY8t"
#     }
    
# users = {
#         "7oDYjo3d9r58EJKYi5x4E8": {
#             "name": "Bob"
#         },
#         "mUP7PpTHmFAkxcQLWKMY8t": {
#             "name": "Alice"
#         },
#     }


