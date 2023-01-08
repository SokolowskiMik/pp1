class TV():
    is_on = False
    channel_no = 1
    channels = []
    volume = 0

    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
            try:
                print(f'TV is on, channel {self.channel_no} ({self.channels[self.channel_no-1]})')
            except:
                print(f'TV is on, channel {self.channel_no}')

            print(f'volume: {self.volume}')

        else:
            print('TV is off')
    
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no
    
    def set_channels(self, channels_list):
        #self.channels = enumerate(channels_list, 1)
        self.channels = channels_list
    def show_channels(self):
        i = 1
        for chan in self.channels:
            print(f'{i}.{chan}', end=' ')
            i += 1
        print()
    
    def increase_volume(self,num):
        self.volume += num
        assert self.volume <= 100
    
    def decrase_volume(self,n):
        self.volume -= n
        assert self.volume >= 0

tv = TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.show_channels()
tv.set_channels(['TVP1','TVP2','Polsat','TVN','Filmbox','Discovery', 'BBC', 'Disney XD'])
tv.show_channels()
tv.increase_volume(10)
tv.show_status()
tv.decrase_volume(2)
tv.show_status()
tv.turn_off()
tv.show_status()



