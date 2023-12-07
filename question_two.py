class Book:
      def __init__(self,title,author,pages):
            # properties
            self.title=title
            self.author=author
            self.pages=pages
    #   method
      def mymtd(self):
            print('Title: ',self.title)
            print('Author: ',self.author)
            print('Pages: ',self.pages)

            # iii)
      def __str__(self):
            return f'{self.author} {self.title}'
      

book1=Book('Riverbetween','PAUL',30)
# displaying title and author only
print(book1)
# displaying the book object information
book1.mymtd()

# ii)
class EBook(Book):
      def __init__(self,title,author,pages,format):
            # additional attribute
            self.format=format
            super().__init__(title,author,pages)
             
     
ebook1=EBook('OliverTwist','amos',23,'PDF')
print(ebook1.title,ebook1.author,ebook1.pages,ebook1.format)

# iv)
# a) A class is a constructor for objects .it is used to create objects
# b)An object an instance of a class
