class TV():
    is_on = False
    channel_no = 1
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
            print(f'TV is on, channel {self.channel_no}')
        else:
            print('TV is off')

tv = TV()
tv.show_status()
tv.turn_on()
tv.show_status()


