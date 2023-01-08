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
        self.channels = enumerate(channels_list, 1)
    def show_channels(self):
        for chan in self.channels:
            print(chan, end=' ')

tv = TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.show_channels()
tv.set_channels(['TVP1','TVP2','Polsat','TVN','Filmbox','Discovery'])
tv.show_channels()
tv.show_status()
tv.turn_off()
tv.show_status()



