from abc import ABC, abstractmethod
class Printable(ABC):

    @abstractmethod
    def print_info(self):
        pass

class Book(Printable):

    def __innit__(self,title,author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f"Book: {self.title} by {self.author}")

book = Book("NNN","F. HHH")
book.print_info()

