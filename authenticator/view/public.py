from fastapi import APIRouter,status
from authenticator.model.dbmodel import Book
from beanie import Save, Insert

router  = APIRouter()

@router.get("/")
async def get_testroute():
    return "OK"

@router.post("/add",status_code=status.HTTP_201_CREATED,response_model=Book)
async def add_book_details(book : Book):
    await book.insert()
    await book.save()
    return book