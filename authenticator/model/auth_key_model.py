from beanie import Document

class AuthKey(Document):
    auth_key: str
    user: str

    class Settings:
        name = "auth_key"



