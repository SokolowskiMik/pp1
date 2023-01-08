class TV():
    is_on = False
    channel_no = 1
    channels = []

    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
            print(f'TV is on, channel {self.channel_no}')
        else:
            print('TV is off')
    
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no
    
    def set_channels(self, channels_list):
        self.channels = channels_list
    def show_channels(self):
        print(self.channels)

tv = TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.set_channel(5)
tv.show_status()
tv.turn_off()
tv.show_status()



