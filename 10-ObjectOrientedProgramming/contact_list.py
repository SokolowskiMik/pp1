import contact

class Contact_List():

    def __init__(self):
        self.contacts = []
    
    def add(self):
        self.contacts.append(contact.create)