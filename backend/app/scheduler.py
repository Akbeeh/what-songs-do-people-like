import asyncio

from app.credentials import auth
from app.database import database


async def update_database():
    while True:
        auth.generate_access_token()
        database.save_top_songs()
        await asyncio.sleep(3600)  # Sleep for 3600 seconds (1 hour)


# Run the function in an asyncio event loop
async def scheduler_update_db():
    asyncio.create_task(update_database())
