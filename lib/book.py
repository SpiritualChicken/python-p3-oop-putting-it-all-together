#!/usr/bin/env python3

class Book:
    def __init__(self, title, initial_page_count):
        self.title = title
        self._page_count = None
        self.page_count = initial_page_count
    

    def get_page(self):
        return self._page_count

    def set_page(self, page_count):
        if type(page_count) in (int, float):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    page_count = property(get_page, set_page)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    

book = Book("And Then There Were None", "273")
# print(book.title)
# print(book.page_count)