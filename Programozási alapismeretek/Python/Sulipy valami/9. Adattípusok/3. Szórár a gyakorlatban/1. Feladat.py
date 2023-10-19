from pprint import pprint

books = []

while True:
    author = input("Szerző: ")
    if not author:
        break
    title = input("Cím: ")

    books.append({"author": author, "title": title})

pprint(books)