class Book:
    status = 'closed'
    current_page = 0
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        #self.pages = pages
        self.status = Book.status
        self.cp = Book.current_page
    def __str__(self):
        return f'book: {self.title}, author: {self.author}, number of pages: {self.pages}'

    def open(self):
        if self.status == 'closed':
            self.status = 'open'
        else:
            print('book already opened')

    def close(self):
        if self.status == 'open':
            self.status == 'close'
        else:
            print('book already closed')

    def read(self):
        page = self.cp
        if self.status == 'open':
            print(f"You are reading page: {page}")
        else:
            print("You can't read this book beacause it is closed")
    
    def next_page(self):
        if self.cp != (self.pages-1) and self.cp != 0:
            self.cp += 1
            print(f'previous page: {self.cp - 1}, current page: {self.cp}, next page: {self.cp + 1}')
        elif self.cp == 0:
            self.cp += 1
            print(f'current page: {self.cp}, next page: {self.cp + 1}')
        elif self.cp == self.pages-1: 
            self.cp += 1
            print(f'You are at the last page {self.cp}')
    
    def prev_page(self):
        if self.cp != 0 or self.cp != self.pages:
            self.cp -= 1
            print(f'previous page: {self.cp - 1}, current page: {self.cp}, next page: {self.cp + 1}')
        elif self.cp == self.pages:
            self.cp -= 1
            print(f'previous page: {self.cp - 1}, current page: {self.cp}')
        else: print('You are at the last page')

class Paper(Book):
    def __init__(self, title, author,pages):
        super().__init__(title,author)
        self.pages = pages
    def __str__(self):
        return f'book: {self.title}, author: {self.author}, number of pages: {self.pages}'
class Ebook(Book):
    def __init__(self, title, author,file):
        super().__init__(title,author)
        self.file = file
    
    def __str__(self):
        return f'book: {self.title}, author: {self.author}, saved in file: {self.file}'

p1 = Paper('łajcik', '2115', '2115')
e1 = Ebook('faw', 'fwaf','fa.jpeg')

print(p1)
print(e1)