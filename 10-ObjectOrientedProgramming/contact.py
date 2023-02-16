class Contact():
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone
        self.contact = {'name': self.name, 'email': self.email, 'telephone': self.telephone}

    def create(self):
        return self.contact