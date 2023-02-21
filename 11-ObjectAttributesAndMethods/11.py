class Phone:
    lock = 'locked'
    off = 'off'
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.status = Phone.off
        self.lock = Phone.lock
    def __str__(self):
        return f'Your phone is: {self.brand} {self.model}'

    def on(self):
        if self.status =='off':
            self.status = 'on'
    def off(self):
        if self.status =='on':
            self.status = 'off'
    def airplane(self):
        if self.status == 'on':
            self.status = 'airplane mode'
    def airplane_off(self):
        if self.status == 'airplane mode':
            self.status = 'on'
    def unlock(self):
        if self.status == 'on':
            self.lock = 'unlocked'
        else: print('phone is off')
    def lock(self):
        if self.status == 'on':
            self.lock = 'locked'
        else: print('phone is off')

    def status(self):
        print(self.status)
    
    def lock(self):
        print(self.lock)
