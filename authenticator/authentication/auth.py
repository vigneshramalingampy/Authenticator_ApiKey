from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from authenticator.model.auth_key_model import AuthKey


api_key_header = APIKeyHeader(name = "X-API-Key")

async def get_user(api_key: str = Security(api_key_header)):
    print(api_key_header)
    if not api_key:
        raise HTTPException(status_code=403, detail="API Key is missing")

    # Find the root user in the database with the provided API key
    root_user = await AuthKey.find_one(AuthKey.auth_key == api_key)
    if not root_user:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    
    return root_user