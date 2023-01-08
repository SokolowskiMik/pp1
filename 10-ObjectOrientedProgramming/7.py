class University():
    def __init__(self):
        self.name = 'CUE'

    def print_name(self):

        print(self.name)
    def set_name(self, name: str):
        self.name = name

uni = University()

uni.print_name()
uni.set_name('MIT')
uni.print_name()