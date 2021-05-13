# start
# Задание 1
# Создайте класс, описывающий книгу. Он должен содержать информацию об авторе,
# названии, годе издания и жанре. Создайте несколько разных книг. Определите
# для него операции проверки на равенство и неравенство, методы __repr__ и __str__.
class Book:
    def book_info(self,author,name,year,ganre):
        self.author=author
        self.name=name
        self.year=year
        self.genre=ganre

        return print(f'{self.author},{self.name},{self.year},{self.genre}')

    def __str__(self):
        pass

    def __repr__(self):
        pass


first_book=Book()
first_book.author='Jonny'
first_book.name='Look at Sun'
first_book.year=2010
first_book.ganre='Drama'

first_book.book_info(first_book.author,first_book.name,first_book.year,first_book.ganre)




