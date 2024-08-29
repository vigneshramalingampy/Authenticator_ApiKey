from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
#from authenticator.authentication.auth import get_user
from authenticator.databases.datamongo import init_db
from authenticator.view import public,private
from authenticator.model.auth_key_model import AuthKey


async def lifespan(app):
    await init_db()
    yield
    print('lifespan end')

def app_run():
    fast_api = FastAPI(lifespan=lifespan)
    fast_api.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return fast_api

app: FastAPI = app_run()

app.include_router(public.router)
app.include_router(private.router)


@app.get("/newuser")
async def newuser():
    user = AuthKey(user="vignesh",auth_key="e54d4431-5dab-474e-b71a-0db1fcb9e659")
    await user.insert()
    await user.save()
    return {"result":"added"}

