class ebook():
    status = 'closed'
    current_page = 0
    def __init__(self, title: str, author: str, n_of_pages: int):
        self.title = title
        self.author = author,
        self.pages = n_of_pages
        self.status = ebook.status
        self.cp = ebook.current_page

    def __str__(self):
        return f'ebook: {self.title}, author: {self.author}, number of pages: {self.pages}'

    def open(self):
        if self.status == 'closed':
            self.status = 'open'
        else:
            print('ebook already opened')

    def close(self):
        if self.status == 'open':
            self.status == 'close'
        else:
            print('ebook already closed')

    def read(self):
        page = self.cp
        if self.status == 'open':
            print(f"You are reading page: {page}")
        else:
            print("You can't read a book beacause it is closed")
    
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
        

book1 = ebook('łajcior','Mike Wazowski',5)
print(book1)
print()
book1.read()
print()
book1.open()
book1.read()
print()
book1.next_page()
book1.read()
print()
book1.next_page()
book1.read()
print()
book1.next_page()
book1.read()
print()
book1.next_page()
book1.read()
print()
book1.next_page()
book1.read()
print()
book1.prev_page()
book1.read()
print()
book1.next_page()
book1.read()
print()
book1.close()
book1.read()

        
    

    