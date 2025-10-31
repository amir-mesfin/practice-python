# Magic method or dunder method (double underscore)


class book:

    def __init__(self, title, author, num_page):
        self.title = title
        self.author = author
        self.num_page = num_page

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __gt__(self, other):
        return self.num_page > other.num_page

    def __lt__(self, other):
        return self.num_page > other.num_page

    def __add__(self, other):
        return self.num_page + other.num_page

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if (key == "title"):
            return self.title
        elif (key == "author"):
            return self.author
        elif (key == "page"):
            return self.num_page
        else:
            return "you inter in correct thing"


book1 = book("abushe lion of the book in the usa", "jjr", 456)
book2 = book("abushe23 tiger in te jungle", "jjr34", 43456)
book3 = book("abushe67 hen in the home ", "jjr456", 453466)

print(book3)
print(book1 == book2)
print(book3 < book2)
print(book1 + book3)
print("abushe" in book1)

print(book3['page'])
