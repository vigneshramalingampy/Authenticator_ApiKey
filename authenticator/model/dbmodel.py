from beanie import Document


class Book(Document):
    title: str
    author: str
    published_year: int
    reviews: list[str] = []

    class Settings:
        name = "books_collection"