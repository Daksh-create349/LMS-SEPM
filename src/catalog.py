"""LMS Catalog Service: ISBN search and title indexing."""

class CatalogService:
    def __init__(self):
        self.inventory = {}

    def add_book(self, isbn: str, title: str, author: str, total_copies: int):
        self.inventory[isbn] = {
            "title": title,
            "author": author,
            "total_copies": total_copies,
            "available_copies": total_copies
        }

    def search_by_isbn(self, isbn: str):
        return self.inventory.get(isbn, None)
