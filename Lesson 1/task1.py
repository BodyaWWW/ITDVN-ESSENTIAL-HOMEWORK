# start
# Задание 1
# Создайте класс, описывающий книгу. Он должен содержать информацию об авторе,
# названии, годе издания и жанре. Создайте несколько разных книг. Определите
# для него операции проверки на равенство и неравенство, методы __repr__ и __str__.
class Comments:
    def comment_info(self,user_name,book_name,comment):
        self.book_name=book_name
        self.user_name=user_name
        self.comment=comment

    def __str__(self):
        return '%s writes about : %s'%(self.user_name,self.book_name,self.comment)






class Book:
    def book_info(self,author,name,year,ganre):
        self.author=author
        self.name=name
        self.year=year
        self.genre=ganre

        # return print(f'{self.author},{self.name},{self.year},{self.genre}')

    def __repr__(self):
        return '%s_%s_%d' % ('_'.join(self.author.split(' ')), '_'.join(self.name.split(' ')), self.year)

    def __str__(self):
        return '%s - %s(%d).%s edition.\nComments:\n%s ' % (self.author, self.name, self.year)


first_book=Book()
first_book.author='Jonny'
first_book.name='Look at Sun'
first_book.year=2010
first_book.ganre='Drama'

first_book.book_info(first_book.author,first_book.name,first_book.year,first_book.ganre)
first_book.__str__()
comm1=Comments()
comm1.user_name='Medison'
comm1.book_name='Look at Sun'
comm1.comment='Amazing book! Easy for read.'
comm1.comment_info(print('Book Comments:'
      '\n user - ',comm1.user_name,
      '\n book -', comm1.book_name,
      '\n comment -',comm1.comment))